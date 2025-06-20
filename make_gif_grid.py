from PIL import Image, ImageSequence
import argparse

def create_gif_grid(input_gif, output_gif, cols, rows):
    # 打开原始GIF
    with Image.open(input_gif) as img:
        # 提取所有帧
        frames = [frame.copy() for frame in ImageSequence.Iterator(img)]

        # 单帧尺寸
        frame_width, frame_height = frames[0].size

        # 输出图像的总尺寸
        total_width = frame_width * cols
        total_height = frame_height * rows

        # 处理每一帧
        new_frames = []
        for frame in frames:
            # 创建新帧
            new_frame = Image.new('RGBA', (total_width, total_height))

            # 将帧按网格布局复制到新帧上
            for y in range(0, total_height, frame_height):
                for x in range(0, total_width, frame_width):
                    new_frame.paste(frame, (x, y))

            new_frames.append(new_frame)

        # 保存所有处理后的帧为一个新的GIF
        new_frames[0].save(output_gif, save_all=True, append_images=new_frames[1:], optimize=False, duration=img.info['duration'], loop=0)

def main():
    parser = argparse.ArgumentParser(description="Create a grid layout GIF from an input GIF.")
    parser.add_argument('-i', '--input', required=True, help="Input GIF file")
    parser.add_argument('-o', '--output', required=False, help="Output GIF file")
    parser.add_argument('-l', '--layout', required=True, help="Grid layout in colsxrows format")

    args = parser.parse_args()

    # 解析布局参数
    try:
        cols, rows = map(int, args.layout.split('x'))
    except ValueError:
        import sys
        print("Error: Layout format should be 'colsxrows' (e.g., 3x2).")
        sys.exit(1)
    print('using config:', args)
    create_gif_grid(args.input, args.output or "output.gif", cols, rows)

if __name__ == "__main__":
    main()