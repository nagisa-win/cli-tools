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

3. 运行脚本

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
这个代码项目是一个包含多种实用命令行工具（Bash/Python）的集合，主要用于图像/视频处理、文件操作和自动化任务。以下是主要功能总结：

---

### **语言/类型占比**
- **Python**：约50%（图像处理、GIF操作、文件合并等）
- **Bash**：约45%（文件操作、依赖管理、自动化脚本）
- **配置文件**：5%（LICENSE/.env等）

---

### **核心功能与重要文件**

#### **1. 图像处理工具**
- **rotate/rotate-imgs** (Bash)  
  功能：生成旋转动画帧/GIF（依赖ImageMagick/ffmpeg）  
  用法：`./rotate -i input.png -o output.gif -f 30`

- **overlay.py** (Python)  
  功能：图像叠加合成  
  用法：`python overlay.py base.png overlay.png output.png`

- **clip-img-color.py** (Python)  
  功能：将指定颜色转为透明  
  用法：`python clip-img-color.py input.png output.png --color 255,255,255`

- **hdr_img.py** (Python)  
  功能：HDR图像处理（需Pillow库）  
  用法：`python hdr_img.py input.jpg output.jpg`

#### **2. GIF/视频工具**
- **make_gif_grid.py** (Python)  
  功能：将GIF分割为网格布局  
  用法：`python make_gif_grid.py input.gif output.gif --cols 2 --rows 2`

- **mkgif** (Bash)  
  功能：将图片序列转为GIF（依赖ffmpeg）  
  用法：`./mkgif -d "frames/%d.png" -o output.gif`

- **merge_videos.py** (Python)  
  功能：合并视频文件  
  用法：`python merge_videos.py input1.mp4 input2.mp4 output.mp4`

#### **3. 文件操作工具**
- **ncmdump** (Bash)  
  功能：批量处理特定格式文件（如音乐缓存解密）  
  用法：`./ncmdump /path/to/files`

- **md5rename** (Bash)  
  功能：用MD5哈希重命名文件  
  用法：`./md5rename file.jpg`

- **copy-my-file.sh** (Bash)  
  功能：备份指定目录/文件到外部存储  
  用法：`./copy-my-file.sh /backup/path`

#### **4. 自动化工具**
- **update_readme.py** (Python)  
  功能：自动生成README（依赖OpenAI API）  
  用法：配置`.env`后运行`python update_readme.py`

- **pyinstxtractor.py** (Python)  
  功能：解包PyInstaller打包的可执行文件  
  用法：`python pyinstxtractor.py packed_executable`

---

### **其他文件**
- **LICENSE**：Apache 2.0开源协议
- **.env**：OpenAI API配置（需保密）
- **README.md**：项目说明与使用指南

---

### **特点**
- 跨平台支持（Bash/Python）
- 依赖常见工具（ImageMagick/ffmpeg/Pillow）
- 模块化设计，每个脚本可独立运行

适合开发者快速完成媒体处理、文件批量操作等任务。
<!--END AI Summary HERE-->
