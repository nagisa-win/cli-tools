# cli-tools

一些有用的命令行脚本 Bash/Python/JS

[@nagisa-win](https://github.com/nagisa-win)

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

#### 主要功能
该项目是一个多功能Python工具集，主要包含以下功能模块：
1. **PyInstaller解包工具** (`pyinstxtractor.py`)：支持提取由PyInstaller打包的可执行文件中的Python脚本和资源文件（支持多个PyInstaller版本）。
2. **图像处理工具**：
   - 图像叠加 (`overlay.py`)：将两张图片叠加生成新图片
   - 颜色透明化 (`clip-img-color.py`)：将图片中指定颜色转为透明
   - GIF网格生成 (`make_gif_grid.py`)：将GIF动画转换为网格排列形式
   - HDR图像处理 (`hdr_img.py`)：高动态范围图像处理
3. **自动化工具**：
   - README生成 (`update_readme.py`)：自动生成项目文档
   - 文件备份 (`copy-my-file.sh`)：备份指定目录和配置文件
   - 环境配置 (`env.sh`)：设置系统环境变量

#### 代码文件结构
```
.
├── pyinstxtractor.py        # PyInstaller解包工具
├── overlay.py               # 图像叠加工具
├── clip-img-color.py        # 图片透明化处理
├── make_gif_grid.py         # GIF网格生成器
├── hdr_img.py               # HDR图像处理器
├── update_readme.py         # README自动生成器
├── copy-my-file.sh          # 文件备份脚本
└── env.sh                   # 环境变量配置脚本
```

#### 使用方法
1. **PyInstaller解包**：
   ```bash
   python pyinstxtractor.py <打包后的exe文件>
   ```

2. **图像处理工具**（通用调用方式）：
   ```bash
   python 脚本名.py [参数]
   # 例如：
   python overlay.py base.png overlay.png output.png
   python clip-img-color.py input.png output.png --color 255,255,255
   ```

3. **自动化工具**：
   - 更新README：
     ```bash
     python update_readme.py
     ```
   - 文件备份：
     ```bash
     ./copy-my-file.sh
     ```
   - 环境配置：
     ```bash
     source env.sh
     ```

#### 技术特点
- 主要基于Python的Pillow库进行图像处理
- 使用argparse模块处理命令行参数
- 包含Shell脚本用于系统级操作
- 支持跨平台运行（Python脚本+Shell脚本）

#### 依赖
- Python 3.x
- Pillow库（图像处理）
- OpenAI API（README生成功能需要）
- Bash环境（Shell脚本）
<!--END AI Summary HERE-->
