#!/usr/bin/env python3
"""
JSON Verification Script
This script reads a JSON file, validates its format, and displays it in a prettier way.
It handles large files and partial JSON content gracefully.
"""

import argparse
import json
import sys
import os
from typing import Any, Optional


def parse_arguments() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Verify and prettify JSON files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python json_verify.py data.json
  python json_verify.py --indent 2 config.json
  python json_verify.py --max-lines 100 large_file.json
        """,
    )

    parser.add_argument("file", help="Path to the JSON file to verify and prettify")

    parser.add_argument(
        "--indent",
        type=int,
        default=2,
        help="Number of spaces for indentation (default: 2)",
    )

    parser.add_argument(
        "--max-lines",
        type=int,
        default=1000,
        help="Maximum number of lines to display for large files (default: 1000)",
    )

    parser.add_argument(
        "--encoding", default="utf-8", help="File encoding (default: utf-8)"
    )

    parser.add_argument(
        "--no-color", action="store_true", help="Disable colored output"
    )

    return parser.parse_args()


def print_colored(text: str, color: str = "reset", use_color: bool = True) -> None:
    """Print colored text to console."""
    if not use_color:
        print(text)
        return

    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "magenta": "\033[95m",
        "cyan": "\033[96m",
        "white": "\033[97m",
        "reset": "\033[0m",
    }

    color_code = colors.get(color, colors["reset"])
    reset_code = colors["reset"]
    print(f"{color_code}{text}{reset_code}")


def read_file_content(file_path: str, encoding: str) -> str:
    """Read file content with error handling."""
    try:
        with open(file_path, "r", encoding=encoding) as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except UnicodeDecodeError as e:
        raise UnicodeDecodeError(f"Encoding error ({encoding}): {e}")
    except PermissionError:
        raise PermissionError(f"Permission denied: {file_path}")
    except Exception as e:
        raise Exception(f"Error reading file: {e}")


def attempt_json_repair(content: str) -> Optional[str]:
    """Attempt to repair common JSON issues."""
    # Try to fix trailing commas
    import re

    # Remove trailing commas before closing brackets/braces
    content = re.sub(r",(\s*[}\]])", r"\1", content)

    # Try to add missing closing brackets/braces
    open_braces = content.count("{") - content.count("}")
    open_brackets = content.count("[") - content.count("]")

    if open_braces > 0:
        content += "}" * open_braces
    if open_brackets > 0:
        content += "]" * open_brackets

    return content


def parse_json_content(content: str) -> tuple[Any, bool, str]:
    """
    Parse JSON content with error handling and repair attempts.
    Returns: (parsed_data, is_valid, error_message)
    """
    # First attempt: try parsing as-is
    try:
        data = json.loads(content)
        return data, True, ""
    except json.JSONDecodeError as e:
        original_error = str(e)

        # Second attempt: try to repair common issues
        try:
            repaired_content = attempt_json_repair(content)
            data = json.loads(repaired_content)
            return (
                data,
                True,
                f"Repaired and parsed successfully (original error: {original_error})",
            )
        except json.JSONDecodeError:
            # Third attempt: try parsing partial content (for truncated files)
            lines = content.split("\n")
            for i in range(len(lines), 0, -10):  # Try removing 10 lines at a time
                try:
                    partial_content = "\n".join(lines[:i])
                    partial_content = attempt_json_repair(partial_content)
                    data = json.loads(partial_content)
                    return (
                        data,
                        False,
                        f"Partial JSON parsed (showing first {i} lines). Original error: {original_error}",
                    )
                except json.JSONDecodeError:
                    continue

            return None, False, f"Invalid JSON: {original_error}"


def truncate_output(json_str: str, max_lines: int) -> tuple[str, bool]:
    """Truncate JSON output if it exceeds max_lines."""
    lines = json_str.split("\n")

    if len(lines) <= max_lines:
        return json_str, False

    truncated_lines = lines[:max_lines]
    truncated_str = "\n".join(truncated_lines)

    # Try to close any open structures in the truncated content
    open_braces = truncated_str.count("{") - truncated_str.count("}")
    open_brackets = truncated_str.count("[") - truncated_str.count("]")

    if open_braces > 0 or open_brackets > 0:
        truncated_str += "\n  ..."
        if open_braces > 0:
            truncated_str += "\n" + "}" * open_braces
        if open_brackets > 0:
            truncated_str += "\n" + "]" * open_brackets

    return truncated_str, True


def main():
    """Main function."""
    try:
        args = parse_arguments()
        use_color = not args.no_color

        # Check if file exists
        if not os.path.isfile(args.file):
            print_colored(
                f"Error: File '{args.file}' does not exist.", "red", use_color
            )
            sys.exit(1)

        # Get file size for information
        file_size = os.path.getsize(args.file)
        print_colored(
            f"Reading file: {args.file} ({file_size:,} bytes)", "blue", use_color
        )

        # Read file content
        try:
            content = read_file_content(args.file, args.encoding)
        except Exception as e:
            print_colored(f"Error: {e}", "red", use_color)
            sys.exit(1)

        # Parse JSON content
        data, is_valid, message = parse_json_content(content)

        if data is None:
            print_colored(f"❌ {message}", "red", use_color)
            sys.exit(1)

        # Display status
        if is_valid:
            if message:
                print_colored(f"⚠️  {message}", "yellow", use_color)
            else:
                print_colored("✅ Valid JSON format", "green", use_color)
        else:
            print_colored(f"⚠️  {message}", "yellow", use_color)

        # Pretty print JSON
        try:
            pretty_json = json.dumps(
                data, indent=args.indent, ensure_ascii=False, sort_keys=True
            )

            # Truncate if necessary
            output, was_truncated = truncate_output(pretty_json, args.max_lines)

            print_colored("\n" + "=" * 50, "cyan", use_color)
            print_colored("PRETTIFIED JSON CONTENT:", "cyan", use_color)
            print_colored("=" * 50, "cyan", use_color)

            print(output)

            if was_truncated:
                print_colored(
                    f"\n⚠️  Output truncated to {args.max_lines} lines",
                    "yellow",
                    use_color,
                )
                print_colored(
                    "Use --max-lines to adjust the limit", "yellow", use_color
                )

            print_colored("\n" + "=" * 50, "cyan", use_color)

        except Exception as e:
            print_colored(f"Error formatting JSON: {e}", "red", use_color)
            sys.exit(1)

    except KeyboardInterrupt:
        print_colored("\n\nOperation cancelled by user.", "yellow", use_color)
        sys.exit(0)
    except Exception as e:
        print_colored(f"Unexpected error: {e}", "red", use_color)
        sys.exit(1)


if __name__ == "__main__":
    main()
