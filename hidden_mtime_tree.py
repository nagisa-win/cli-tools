#!/usr/bin/env python3

import argparse
import os
import re
import stat
import sys
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from pathlib import Path


@dataclass
class Node:
    path: Path
    is_dir: bool
    depth: int
    display_name: str
    effective_mtime: float
    direct_mtime: float
    children: list["Node"] = field(default_factory=list)
    error: str | None = None


def format_mtime(ts: float) -> str:
    return datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")


def parse_relative_time(value: str) -> datetime:
    if not value:
        raise ValueError("expected format like 1y, 1m, 1d, 1h, or 1m15d")

    delta = timedelta()
    position = 0
    for match in re.finditer(r"(\d+)(y|m|d|h)", value):
        if match.start() != position:
            raise ValueError("expected format like 1y, 1m, 1d, 1h, or 1m15d")

        amount = int(match.group(1))
        unit = match.group(2)
        if unit == "y":
            delta += timedelta(days=365 * amount)
        elif unit == "m":
            delta += timedelta(days=30 * amount)
        elif unit == "d":
            delta += timedelta(days=amount)
        else:
            delta += timedelta(hours=amount)
        position = match.end()

    if position != len(value):
        raise ValueError("expected format like 1y, 1m, 1d, 1h, or 1m15d")

    return datetime.now() - delta


def is_hidden_name(name: str) -> bool:
    return name.startswith(".")


def safe_lstat(path: Path) -> os.stat_result | None:
    try:
        return path.lstat()
    except OSError:
        return None


def build_node(path: Path, depth: int, max_depth: int) -> Node:
    st = safe_lstat(path)
    if st is None:
        return Node(
            path=path,
            is_dir=False,
            depth=depth,
            display_name=path.name,
            effective_mtime=0.0,
            direct_mtime=0.0,
            error="unreadable",
        )

    is_dir = stat.S_ISDIR(st.st_mode)
    node = Node(
        path=path,
        is_dir=is_dir,
        depth=depth,
        display_name=path.name,
        effective_mtime=st.st_mtime,
        direct_mtime=st.st_mtime,
    )

    if not is_dir:
        return node

    try:
        entries = list(os.scandir(path))
    except OSError as exc:
        node.error = str(exc)
        return node

    child_hidden_nodes: list[Node] = []
    latest_mtime = node.effective_mtime

    for entry in entries:
        try:
            entry_stat = entry.stat(follow_symlinks=False)
        except OSError:
            continue

        latest_mtime = max(latest_mtime, entry_stat.st_mtime)
        entry_path = Path(entry.path)

        if entry.is_dir(follow_symlinks=False):
            child_node = build_node(entry_path, depth + 1, max_depth)
            latest_mtime = max(latest_mtime, child_node.effective_mtime)
            if is_hidden_name(entry.name) and depth < max_depth:
                child_hidden_nodes.append(child_node)

    node.effective_mtime = latest_mtime
    node.children = sorted(
        child_hidden_nodes,
        key=lambda child: (child.effective_mtime, child.display_name.lower()),
    )
    return node


def print_tree(node: Node, prefix: str = "", is_last: bool = True) -> None:
    branch = "└── " if is_last else "├── "
    kind = "/" if node.is_dir else ""
    details = format_mtime(node.effective_mtime) if node.effective_mtime else "N/A"
    if node.error:
        details = f"{details} [error: {node.error}]"
    print(f"{prefix}{branch}{node.display_name}{kind} [{details}]")

    next_prefix = prefix + ("    " if is_last else "│   ")
    for index, child in enumerate(node.children):
        print_tree(child, next_prefix, index == len(node.children) - 1)


def trash_target(path: Path, trash_dir: Path) -> Path:
    target = trash_dir / path.name
    if not target.exists():
        return target

    stamp = datetime.now().strftime("%Y%m%d%H%M%S")
    for index in range(1, 1000):
        candidate = trash_dir / f"{path.name}.{stamp}.{index}"
        if not candidate.exists():
            return candidate

    raise RuntimeError(f"failed to find available Trash name for {path}")


def move_to_trash(nodes: list[Node], trash_dir: Path) -> int:
    trash_dir.mkdir(exist_ok=True)
    moved = 0
    for node in nodes:
        target = trash_target(node.path, trash_dir)
        try:
            node.path.rename(target)
        except OSError as exc:
            print(f"Failed to move {node.path} to Trash: {exc}", file=sys.stderr)
            continue
        print(f"Moved to Trash: {node.path} -> {target}")
        moved += 1
    return moved


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Print a hidden-file tree with effective mtimes. A directory's displayed "
            "mtime is the latest mtime found anywhere in its full subtree."
        )
    )
    parser.add_argument("root", nargs="?", default=str(Path.home()))
    parser.add_argument("--max-depth", type=int, default=3)
    parser.add_argument(
        "--clean",
        metavar="RELATIVE_TIME",
        help="move top-level hidden dirs older than this to ~/.Trash, e.g. 1y, 1m, 1d, 1h, 1m15d",
    )
    parser.add_argument("--yes", action="store_true", help="skip confirmation for --clean")
    args = parser.parse_args()

    root = Path(args.root).expanduser().resolve()
    if not root.exists():
        print(f"Path does not exist: {root}", file=sys.stderr)
        return 1

    if args.max_depth < 0:
        print("--max-depth must be >= 0", file=sys.stderr)
        return 1

    try:
        entries = list(os.scandir(root))
    except OSError as exc:
        print(f"Failed to read {root}: {exc}", file=sys.stderr)
        return 1

    roots: list[Node] = []
    for entry in entries:
        if not is_hidden_name(entry.name):
            continue

        entry_path = Path(entry.path)
        if entry.is_dir(follow_symlinks=False):
            roots.append(build_node(entry_path, 1, args.max_depth))

    roots.sort(key=lambda node: (node.effective_mtime, node.display_name.lower()))

    if args.clean:
        try:
            cutoff = parse_relative_time(args.clean)
        except ValueError as exc:
            print(f"Invalid --clean value: {exc}", file=sys.stderr)
            return 1

        trash_dir = root / ".Trash"
        candidates = [
            node
            for node in roots
            if node.path != trash_dir
            and node.effective_mtime
            and datetime.fromtimestamp(node.effective_mtime) < cutoff
        ]

        print(f"Clean candidates for {root} older than {args.clean} ({format_mtime(cutoff.timestamp())}):")
        if not candidates:
            print("No top-level hidden directories matched.")
            return 0

        for node in candidates:
            print(f"- {node.path} [{format_mtime(node.effective_mtime)}]")

        if not args.yes:
            answer = input("Move these directories to ~/.Trash? Type 'yes' to continue: ")
            if answer != "yes":
                print("Cancelled.")
                return 0

        moved = move_to_trash(candidates, trash_dir)
        print(f"Moved {moved}/{len(candidates)} directories to Trash.")
        return 0

    print(f"Hidden tree for {root} (max_depth={args.max_depth})")
    for index, node in enumerate(roots):
        print_tree(node, "", index == len(roots) - 1)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
