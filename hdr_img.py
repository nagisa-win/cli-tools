#!/usr/bin/env python3
#coding=utf-8

import sys
import os

try:
    from PIL import Image
except ImportError:
    print("错误：需要安装Pillow库。请使用以下命令安装：")
    print("pip install Pillow")
    sys.exit(1)


def main():
    if len(sys.argv) < 2 or len(sys.argv) > 4:
        print(f"用法: {sys.argv[0]} <输入> <ICC文件> <输出>")
        sys.exit(1)

    icc_file = "~/workspace/HDR_IMG/HDR.icc"
    if len(sys.argv) == 4:
        input_img, icc_file, output_img = sys.argv[1:4]
    if len(sys.argv) == 3:
        input_img, icc_file = sys.argv[1:3]
        raw_name, ext = os.path.splitext(input_img)
        output_img = f"{raw_name}_hdr{ext}"
    if len(sys.argv) == 2:
        input_img = sys.argv[1]
        raw_name, ext = os.path.splitext(input_img)
        output_img = f"{raw_name}_hdr{ext}"

    # 验证输入文件
    for path in [input_img, icc_file]:
        if not os.path.isfile(path):
            print(f"错误：文件不存在 - {path}")
            sys.exit(1)

    # 读取ICC配置文件
    try:
        with open(icc_file, "rb") as f:
            icc_data = f.read()
    except Exception as e:
        print(f"读取ICC配置文件失败: {str(e)}")
        sys.exit(1)

    # 处理图像
    try:
        with Image.open(input_img) as img:
            img.save(output_img, icc_profile=icc_data)
            print(f"成功生成图像: {output_img} ICC={os.path.basename(icc_file)}")
    except Exception as e:
        print(f"图像处理失败: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
