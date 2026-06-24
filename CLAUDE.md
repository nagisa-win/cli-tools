# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目简介

这是一个个人命令行工具集合，包含 Bash / Python / JavaScript 脚本，涵盖媒体处理、文件操作、AI 辅助等功能。

## 常用命令

### Lint（CI 也会执行）
```bash
pylint $(git ls-files '*.py')
```

### 更新 README.md（需先 git commit，再运行）
```bash
# 1. 配置 .env（参考 .env.example）
pip install python-dotenv openai chardet
# 2. 提交变更后执行
python update_readme.py
```

## 架构说明

- 所有工具均为独立脚本，无公共依赖库，直接运行即可。
- `bin/` 存放预编译二进制工具（ncmdump、pycdc 等），不参与 Python lint。
- `update_readme.py` 是唯一的"元脚本"：读取所有文件内容，调用 OpenAI 兼容 API 生成摘要，用正则替换 README.md 中的 `<!--START ... HERE-->` 占位区块，然后 `git commit --amend`，最后还原 README 原始内容（避免把生成内容提交进仓库）。
- `.env` 中的 `AI_API_KEY` / `AI_BASE_URL` / `AI_MODEL` 供 `update_readme.py` 使用，不得提交。

## 新增脚本规范

- 文件名用小写 + 连字符（shell/无扩展名）或下划线（`.py`）。
- Python 脚本需兼容 3.8 ~ 3.10（见 CI matrix）。
- 新增脚本后在 README.md 的占位区块内手动补充说明，或重新运行 `update_readme.py`。
