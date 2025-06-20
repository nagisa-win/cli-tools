# coding=utf-8

import sys
from PIL import Image, ImageSequence
import argparse

def overlay_images(base_path, overlay_path, output_path):
    # 打开底图和覆盖图
    base_image = Image.open(base_path)
    overlay_image = Image.open(overlay_path)
    
    # 获取底图的模式
    mode = base_image.mode
    
    # 对覆盖图进行缩放
    base_size = base_image.size
    overlay_image = overlay_image.resize(base_size, Image.LANCZOS)

    # 根据底图类型处理
    if "gif" in base_path:
        print(f"GIF: {base_path}")
        frames = []
        # 处理每一帧
        for frame in ImageSequence.Iterator(base_image):
            frame = frame.convert("RGBA")
            # 合成图片
            merged_frame = Image.alpha_composite(frame, overlay_image)
            # 转回原始模式
            merged_frame = merged_frame.convert(mode)
            frames.append(merged_frame)
        
        # 保存GIF
        frames[0].save(output_path, save_all=True, append_images=frames[1:], loop=0)
    else:
        print(f"STATIC: {base_path}")
        # 如果是静态图片，直接合成
        base_image = base_image.convert("RGBA")
        merged_image = Image.alpha_composite(base_image, overlay_image)
        merged_image = merged_image.convert(mode)
        merged_image.save(output_path)

def main():
    parser = argparse.ArgumentParser(description='Overlay an image onto a base image.')
    parser.add_argument('-i', nargs=2, help='<base image> <overlay image>', required=True)
    parser.add_argument('-o', help='<output file>', required=True)
    
    args = parser.parse_args()

    base_path = args.i[0]
    overlay_path = args.i[1]
    output_path = args.o

    overlay_images(base_path, overlay_path, output_path)

if __name__ == '__main__':
    main()
