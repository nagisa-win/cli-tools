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
这个代码项目包含多个独立的Python和Shell脚本工具，主要功能涉及图像处理、文件操作和项目维护。以下是主要总结：

---

### **主要代码文件结构及功能**
1. **图像处理工具**：
   - `overlay.py`：图像叠加工具（使用PIL库处理多图叠加）
   - `clip-img-color.py`：将图片中指定颜色转为透明（基于PIL）
   - `make_gif_grid.py`：将GIF动画转换为网格布局的GIF（支持行列配置）
   - `hdr_img.py`：HDR（高动态范围）图像处理工具（依赖PIL）

2. **PyInstaller相关工具**：
   - `pyinstxtractor.py`：PyInstaller解包工具（支持提取PyInstaller 6.x打包的二进制文件）

3. **项目维护工具**：
   - `update_readme.py`：通过OpenAI API自动更新README文件（需配置API密钥）
   - `copy-my-file.sh`：文件同步脚本（将指定目录文件同步到目标路径，如外接存储）
   - `env.sh`：环境变量配置脚本（为项目设置系统环境变量）

---

### **主要功能**
- **图像处理**：支持透明化、GIF编辑、HDR处理和图像叠加。
- **逆向工程**：解包PyInstaller生成的二进制文件。
- **自动化维护**：README生成、文件同步和环境配置。

---

### **使用方法**
1. **图像工具**：
   ```bash
   python3 clip-img-color.py -i input.png -c "#FFFFFF" -o output.png  # 颜色透明化
   python3 make_gif_grid.py input.gif output.gif --cols 2            # 生成网格GIF
   ```
2. **PyInstaller解包**：
   ```bash
   python3 pyinstxtractor.py packed_executable
   ```
3. **文件同步**：
   ```bash
   bash copy-my-file.sh  # 同步文件到默认路径（需配置SOURCE_LIST）
   ```
4. **README更新**：
   ```bash
   python3 update_readme.py  # 需提前配置OpenAI API密钥（.env文件）
   ```

---

### **依赖项**
- Python库：`Pillow (PIL)`、`openai`、`python-dotenv`
- 系统：部分脚本需Linux/macOS环境（如Shell脚本）。

项目工具独立性强，可按需单独使用，适合开发者和图像处理场景。
<!--END AI Summary HERE-->
