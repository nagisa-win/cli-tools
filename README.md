# cli-tools

一些有用的命令行脚本 Bash/Python/JS

[@nagisa-win](https://github.com/nagisa-win)

## 添加git commit hook

```bash
chmod +x pre-commit.py && git config core.hooksPath . && ln -sf ../../pre-commit.py .git/hooks/pre-commit
```

即可自动生成以下内容～

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
    pre-commit.py
    pyinstxtractor.py
    rotate
    rotate-imgs
```
<!--END Tree of Files HERE-->

## 项目摘要
<!--START AI Summary HERE-->
This project, "cli-tools", provides a collection of useful command-line scripts in Bash, Python, and potentially JS, including functionalities such as extracting PyInstaller-packed executables, overlaying images, converting specific image colors to transparent, generating text using OpenAI's API, creating GIF grids, and more, along with bash scripts for file manipulation and environment variable setup.
<!--END AI Summary HERE-->
