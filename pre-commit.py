#!/usr/bin/env python3

import os
import re
import openai
from dotenv import load_dotenv


def generate_file_tree():
    """Generate project file tree"""
    file_tree = []
    for root, dirs, files in os.walk("."):
        # Skip hidden directories, node_modules and bin
        dirs[:] = [
            d
            for d in dirs
            if not d.startswith(".") and d not in ["node_modules", "bin"]
        ]
        level = root.count(os.sep)
        indent = " " * 4 * level
        file_tree.append(f"{indent}{os.path.basename(root)}/")
        subindent = " " * 4 * (level + 1)
        for f in sorted(files):
            if not f.startswith("."):
                file_tree.append(f"{subindent}{f}")
    return "```\n" + "\n".join(file_tree) + "\n```"


def generate_ai_summary():
    """Generate project summary using AI"""
    load_dotenv()
    openai.api_key = os.getenv("AI_API_KEY")
    openai.api_base = os.getenv("AI_BASE_URL")
    if not openai.api_key or not openai.api_base:
        print("AI_API_KEY or AI_BASE_URL is not set in .env file")
        return

    # Collect all non-binary files
    file_contents = []
    for root, _, files in os.walk("."):
        if "bin" in root.split(os.sep):
            continue
        for file in files:
            if file.endswith((".py", ".sh", ".md")):  # Skip binary files
                try:
                    with open(os.path.join(root, file), "r") as f:
                        content = f.read(1000)  # Read first 1000 chars
                        file_contents.append(f"{file}: {content[:100]}...")
                except:
                    continue

    prompt = f"""请简要总结这个代码项目的主要功能，包括主要代码文件结构、主要功能和使用方法。文件内容如下：
    {file_contents}
    """

    client = openai.OpenAI(
        api_key=os.getenv("AI_API_KEY"), base_url=os.getenv("AI_BASE_URL")
    )
    response = client.chat.completions.create(
        model=os.getenv("AI_MODEL"), messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


def update_readme(file_tree, ai_summary):
    """Update README.md with new file tree and AI summary"""
    with open("README.md", "r") as f:
        content = f.read()

    # Update file tree
    pattern = r"(<!--START Tree of Files HERE-->)(.*?)(<!--END Tree of Files HERE-->)"
    updated_content = re.sub(pattern, rf"\1\n{file_tree}\n\3", content, flags=re.DOTALL)

    # Update AI summary
    pattern = r"(<!--START AI Summary HERE-->)(.*?)(<!--END AI Summary HERE-->)"
    updated_content = re.sub(
        pattern, rf"\1\n{ai_summary}\n\3", updated_content, flags=re.DOTALL
    )

    with open("README.md", "w") as f:
        f.write(updated_content)


if __name__ == "__main__":
    file_tree = generate_file_tree()
    ai_summary = generate_ai_summary()
    update_readme(file_tree, ai_summary)
    # Stage the updated README.md
    os.system("git add README.md")
