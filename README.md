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

该项目是一个**命令行工具集合**，主要包含用于图像处理、文件操作和系统管理的脚本，语言以**Bash和Python**为主。

#### 语言/类型占比
- **Bash脚本**：约60%（如rotate、ncmdump、copy-my-file.sh等）
- **Python脚本**：约35%（如pyinstxtractor.py、overlay.py等）
- **配置文件/其他**：约5%（如.gitignore、LICENSE等）

---

### 重要文件及功能

#### 1. **PyInstaller解包工具** (`pyinstxtractor.py`)
- **功能**：提取PyInstaller打包的可执行文件中的Python源码，支持多个版本。
- **使用**：  
  ```bash
  python pyinstxtractor.py <打包后的exe文件>
  ```

#### 2. **图像处理工具**
- **overlay.py** (Python)  
  - 功能：叠加两张图片（底图+覆盖图）  
  - 使用：  
    ```bash
    python overlay.py -b 底图.png -o 覆盖图.png -r 输出.png
    ```

- **clip-img-color.py** (Python)  
  - 功能：将图片中指定颜色转为透明  
  - 使用：  
    ```bash
    python clip-img-color.py -i 输入.png -o 输出.png -c 255,255,255
    ```

- **rotate-imgs** (Bash)  
  - 功能：生成旋转动画帧（依赖ImageMagick）  
  - 使用：  
    ```bash
    ./rotate-imgs -i input.png -o frames_ -a 10
    ```

#### 3. **GIF相关工具**
- **make_gif_grid.py** (Python)  
  - 功能：将GIF分割为网格布局  
  - 使用：  
    ```bash
    python make_gif_grid.py -i input.gif -o output.gif -c 3 -r 2
    ```

- **mkgif** (Bash)  
  - 功能：将图片序列合成GIF（依赖ffmpeg）  
  - 使用：  
    ```bash
    ./mkgif -d "frames_%d.png" -f 30 -o output.gif
    ```

#### 4. **文件操作工具**
- **ncmdump** (Bash)  
  - 功能：批量解密网易云音乐NCM格式文件  
  - 使用：  
    ```bash
    ./ncmdump <音乐目录>
    ```

- **md5rename** (Bash)  
  - 功能：用MD5哈希值重命名文件  
  - 使用：  
    ```bash
    ./md5rename 文件.jpg
    ```

#### 5. **系统工具**
- **copy-my-file.sh** (Bash)  
  - 功能：备份指定目录/文件到外部存储  
  - 使用：  
    ```bash
    ./copy-my-file.sh /目标/路径
    ```

- **env.sh** (Bash)  
  - 功能：设置系统环境变量  
  - 使用：  
    ```bash
    source env.sh
    ```

#### 6. **自动化工具**
- **update_readme.py** (Python)  
  - 功能：自动生成README.md（依赖OpenAI API）  
  - 使用：  
    ```bash
    python update_readme.py
    ```

---

### 其他说明
- **依赖管理**：部分脚本需安装ImageMagick、ffmpeg、Pillow等库。
- **许可证**：Apache 2.0（见LICENSE文件）。
- **配置**：需在`.env`中设置OpenAI API密钥以使用README生成功能。

项目适合**开发者和系统管理员**快速处理图像、文件或自动化任务。
<!--END AI Summary HERE-->
