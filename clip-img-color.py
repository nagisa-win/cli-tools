#!/usr/bin/env python3
# coding=utf-8

from PIL import Image
import argparse


def make_color_transparent(input_path, output_path, color=(255, 255, 255), tolerance=0):
    """
    将图片中指定颜色的像素转换为透明
    :param input_path: 输入图片路径
    :param output_path: 输出图片路径
    :param color: 要转换的RGB颜色元组 (默认白色)
    :param tolerance: 颜色容差范围 (0-255)
    """
    try:
        # 打开图片并转换为RGBA模式
        img = Image.open(input_path)
        img = img.convert("RGBA")

        # 获取像素数据
        datas = img.getdata()

        # 创建新像素列表
        new_data = []
        for item in datas:
            # 检查当前像素颜色是否在目标颜色容差范围内
            if all(abs(item[i] - color[i]) <= tolerance for i in range(3)):
                # 将符合条件的像素设置为完全透明
                new_data.append((255, 255, 255, 0))
            else:
                # 保留其他像素
                new_data.append(item)

        # 更新图片数据
        img.putdata(new_data)

        # 保存处理后的图片
        img.save(output_path, "PNG")
        print(f"图片已成功保存至: {output_path}")

    except Exception as e:
        print(f"处理过程中发生错误: {str(e)}")


if __name__ == "__main__":
    # 设置命令行参数
    parser = argparse.ArgumentParser(description="将PNG图片中的指定颜色转换为透明")
    parser.add_argument("input", help="输入图片路径")
    parser.add_argument(
        "-o", "--output", help="输出图片路径（默认：输入文件_transparent.png）"
    )
    parser.add_argument(
        "-c", "--color", help="目标颜色（格式：R,G,B 例如：255,255,255）"
    )
    parser.add_argument(
        "-t", "--tolerance", type=int, default=0, help="颜色容差值（0-255，默认：0）"
    )

    args = parser.parse_args()

    # 设置输出路径
    output_path = args.output or args.input.replace(".png", "_transparent.png")

    # 处理颜色参数
    if args.color:
        try:
            color = tuple(map(int, args.color.split(",")))
            if len(color) != 3 or not all(0 <= c <= 255 for c in color):
                raise ValueError
        except:
            print("错误：颜色格式无效，请使用 R,G,B 格式（例如：255,0,0）")
            exit(1)
    else:
        color = (255, 255, 255)  # 默认白色

    # 检查容差值范围
    if not 0 <= args.tolerance <= 255:
        print("错误：容差值必须在0-255范围内")
        exit(1)

    # 执行转换
    make_color_transparent(args.input, output_path, color, args.tolerance)
