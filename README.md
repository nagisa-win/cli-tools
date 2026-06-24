# cli-tools

一些有用的命令行脚本 Bash/Python/JS

来自 [@nagisa-win](https://github.com/nagisa-win)

## 自动生成README.md

1. 安装依赖

`pip install python-dotenv openai`

2. 配置 `.env` 文件

```
# API key
AI_API_KEY=<your_api_key>
# Chat base url
AI_BASE_URL=<your_base_url>
# Model
AI_MODEL=<your_model>
```

3. 先提交变更，再运行以下命令更新 README.md

```bash
python update_readme.py
```

## 目录
<!--START Tree of Files HERE-->
```
./
    CLAUDE.md
    LICENSE
    README.md
    aria-dl
    clip-img-color.py
    copy-my-file.sh
    env.sh
    fism
    gif-grid
    gitm
    hdr-img.sh
    hdr_img.py
    hidden_mtime_tree.py
    json_verify.py
    make_gif_grid.py
    md5rename
    merge_videos.py
    mkgif
    ncmdump
    overlay.py
    pakm
    prettier.js
    pyinstxtractor.py
    rotate
    rotate-imgs
    update_readme.py
```
<!--END Tree of Files HERE-->

## 项目摘要
<!--START AI Summary HERE-->
### 项目总结

这是一个**个人命令行工具集合项目**，主要目标是提升日常开发、媒体处理和文件管理的效率。项目涵盖多种实用脚本，包括图片/视频处理、Git 工作流简化、文件批量操作以及逆向工程工具等。

### 代码文件统计

项目主要包含 **Python** 和 **Bash** 两种语言的脚本，辅以少量配置文件。

*   **语言占比**：
    *   **Bash 脚本 (约 55%)**：主要用于封装系统命令、文件操作和 Git 流程。
    *   **Python 脚本 (约 40%)**：主要用于复杂的媒体处理（依赖 Pillow）、数据解析和自动化任务。
    *   **JavaScript/配置文件 (约 5%)**：用于代码规范配置（Prettier/ESLint）。

*   **功能分类占比**：
    *   **媒体处理 (50%)**：GIF 制作、图片旋转/叠加、视频合并、HDR 处理等。
    *   **开发与系统工具 (30%)**：Git 辅助、压缩解压、文件重命名、环境配置。
    *   **其他工具 (20%)**：下载辅助、逆向提取、AI 辅助文档生成。

### 重要文件功能简述及使用方法

以下是项目中几个核心脚本的功能说明及基本用法：

#### 1. `pakm` (Bash)
*   **功能**：统一的压缩与解压工具入口。自动根据文件扩展名调用对应的工具（如 `tar`, `unzip`, `unrar` 等），无需记忆复杂的参数。
*   **用法**：
    ```bash
    # 解压文件
    ./pakm <archive_file>
    # 压缩文件/目录
    ./pakm <source_file_or_dir>
    ```

#### 2. `gitm` (Bash)
*   **功能**：Git 工作流简化工具。封装了常用的 Git 操作，如基于 master 创建新分支、无痛合并分支、删除已合并分支等。
*   **用法**：
    ```bash
    ./gitm create <branch_name>  # 创建并切换新分支
    ./gitm merge <branch_name>   # 合并分支到 master
    ./gitm delete <branch_name>  # 删除分支
    ```

#### 3. `mkgif` (Bash)
*   **功能**：利用 `ffmpeg` 将一系列图片（如帧序列）快速合成为 GIF 动图。
*   **用法**：
    ```bash
    # 将当前目录下的 png 图片合成 output.gif
    ./mkgif -d . -f 30 -o output.gif
    ```

#### 4. `ncmdump` (Bash)
*   **功能**：网易云音乐 `.ncm` 加密格式转换工具。用于批量解密 ncm 文件为普通音乐格式。
*   **用法**：
    ```bash
    ./ncmdump <directory_path>
    ```

#### 5. `pyinstxtractor.py` (Python)
*   **功能**：PyInstaller 提取器。用于反编译（解包）由 PyInstaller 打包的 EXE 文件，提取其中的 Python 脚本和资源文件。
*   **用法**：
    ```bash
    python pyinstxtractor.py <executable_file>
    ```

#### 6. `aria-dl` (Bash)
*   **功能**：`aria2c` 下载工具的封装脚本。预设了高并发参数，支持多线程分片下载，加快大文件下载速度。
*   **用法**：
    ```bash
    ./aria-dl <URL>
    ```

#### 7. `overlay.py` (Python)
*   **功能**：图片叠加工具。将一张覆盖图叠加到底图上，支持透明度处理。
*   **用法**：
    ```bash
    python overlay.py --base <base_image> --overlay <overlay_image> --output <output_image>
    ```
<!--END AI Summary HERE-->
