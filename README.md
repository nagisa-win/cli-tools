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
这个代码项目是一个包含多种命令行工具的集合，主要用于图像处理、视频处理、文件操作等任务。以下是主要功能和文件分析：

### 语言/类型占比
- **Python**: 约45%（9个文件）
- **Bash脚本**: 约45%（9个文件）
- **配置文件/其他**: 约10%（LICENSE、README等）

### 主要功能分类
1. **图像处理**（GIF/PNG操作）
2. **视频处理**（合并/转换）
3. **文件操作**（解包/重命名/同步）
4. **开发工具**（README生成/PyInstaller解包）

### 重要文件说明

#### 核心工具
1. **pyinstxtractor.py**  
   - 功能：PyInstaller解包工具（支持多个版本）
   - 使用：`python pyinstxtractor.py <打包文件>`

2. **overlay.py**  
   - 功能：图像叠加合成
   - 使用：`python overlay.py 底图.png 覆盖图.png 输出.png`

3. **merge_videos.py**  
   - 功能：视频合并（支持B站缓存拼接）
   - 使用：`python merge_videos.py 输入目录 输出文件`

#### 图像处理脚本
1. **rotate-imgs** (Bash)  
   - 功能：生成旋转动画帧
   - 依赖：ImageMagick/ffmpeg  
   - 使用：`./rotate-imgs -i input.png -o frames_`

2. **make_gif_grid.py**  
   - 功能：将GIF排列成网格
   - 使用：`python make_gif_grid.py input.gif output.gif 3x2`

3. **clip-img-color.py**  
   - 功能：图片背景透明化
   - 使用：`python clip-img-color.py input.png output.png`

#### 实用工具
1. **ncmdump** (Bash)  
   - 功能：音乐文件格式转换
   - 使用：`./ncmdump 音乐目录`

2. **md5rename** (Bash)  
   - 功能：用MD5哈希重命名文件
   - 使用：`./md5rename 文件名`

3. **update_readme.py**  
   - 功能：自动生成README（需OpenAI API）
   - 配置：需设置`.env`中的API密钥

### 典型工作流
```bash
# 图像处理示例
./rotate-imgs -i logo.png | python make_gif_grid.py - output.gif 2x2

# 开发辅助
python update_readme.py  # 更新文档
python pyinstxtractor.py packaged_app.exe  # 逆向分析
```

项目采用Apache 2.0许可证，主要依赖Pillow(Python)和ImageMagick/ffmpeg(Bash)。通过组合这些脚本可以快速完成多媒体处理和文件操作任务。
<!--END AI Summary HERE-->
