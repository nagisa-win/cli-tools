# cli-tools

一些有用的命令行脚本 Bash/Python/JS

[@nagisa-win](https://github.com/nagisa-win)

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
    LICENSE
    README.md
    clip-img-color.py
    copy-my-file.sh
    env.sh
    fism
    gif-grid
    hdr_img.py
    make_gif_grid.py
    md5rename
    merge_videos.py
    mkgif
    ncmdump
    overlay.py
    pyinstxtractor.py
    rotate
    rotate-imgs
    update_readme.py
```
<!--END Tree of Files HERE-->

## 项目摘要
<!--START AI Summary HERE-->
### 项目总结

该项目是一个包含多种实用命令行工具（Bash/Python）的集合，主要用于图像/视频处理、文件操作和自动化任务。主要语言为Python和Bash脚本。

#### 语言/类型占比
- **Python**: 约45%（图像处理、GIF生成、文件合并等）
- **Bash**: 约45%（文件操作、依赖安装、批量处理等）
- **配置文件/其他**: 约10%（LICENSE、README、Git相关文件）

---

### 重要文件及功能

#### 核心工具
1. **pyinstxtractor.py**  
   - **功能**: PyInstaller解包工具，支持多种版本的可执行文件提取  
   - **使用**: `python pyinstxtractor.py <pyinstaller生成的可执行文件>`

2. **图像处理工具组**  
   - `overlay.py` - 图像叠加合成  
     ```bash
     python overlay.py base.png overlay.png output.png
     ```
   - `clip-img-color.py` - 图片颜色透明化处理  
   - `hdr_img.py` - HDR图像处理  
   - `rotate`/`rotate-imgs` - 图像旋转生成GIF（依赖ImageMagick）

3. **GIF相关工具**  
   - `make_gif_grid.py` - 将多个GIF合并为网格布局  
   - `mkgif` - 通过图片序列生成GIF（依赖ffmpeg）

4. **视频处理**  
   - `merge_videos.py` - 视频合并工具（支持文件名清洗和格式转换）

5. **文件操作**  
   - `ncmdump` - 批量处理NCM音乐文件  
   - `md5rename` - 用MD5哈希重命名文件  
   - `copy-my-file.sh` - 自动化文件备份脚本

---

#### 支持文件
- **README.md**: 项目说明，包含自动生成README的指南  
- **update_readme.py**: 通过OpenAI自动生成项目文档（需配置`.env`中的API_KEY）  
- **LICENSE**: Apache 2.0开源协议  
- **pylint.yml**: GitHub Actions的Python代码检查配置  

---

### 使用流程
1. 安装依赖：  
   ```bash
   pip install Pillow openai python-dotenv
   brew install imagemagick ffmpeg  # macOS用户
   ```
2. 复制`.env.example`为`.env`并填写API配置（如需使用AI生成文档）  
3. 直接运行对应脚本，例如：  
   ```bash
   ./rotate -i input.png -o output.gif
   python merge_videos.py /path/to/videos
   ```

项目强调命令行自动化，适合批量处理媒体文件或集成到CI/CD流程中。
<!--END AI Summary HERE-->
