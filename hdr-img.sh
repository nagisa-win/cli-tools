#!/bin/bash

# 检查ImageMagick是否安装
check_dependencies() {
    if ! command -v magick &> /dev/null; then
        if ! command -v convert &> /dev/null; then
            echo "错误: ImageMagick未安装"
            echo "在macOS上使用: brew install imagemagick"
            echo "在Linux上使用: sudo apt-get install imagemagick (Debian/Ubuntu)"
            echo "或: sudo yum install imagemagick (RHEL/CentOS)"
            exit 1
        fi
    fi
}

# 显示帮助信息
show_help() {
    echo "用法: $0 [输入文件] [输出文件]"
    echo "将PNG图片转换为HDR效果"
    echo "示例:"
    echo "  $0 input.png"
    echo "  $0 input.png output.png"
    exit 0
}

# 应用HDR效果
apply_hdr() {
    local input="$1"
    local output="$2"

    # 检查ICC文件是否存在
    icc_file="ITUR_2100_PQ_FULL.icc"
    if [ ! -f "$icc_file" ]; then
        echo "错误: ICC配置文件 $icc_file 未找到"
        echo "请确保ITUR_2100_PQ_FULL.icc文件存在于当前目录"
        exit 1
    fi

    # 检查ICC文件是否存在
    icc_file="ITUR_2100_PQ_FULL.icc"
    if [ ! -f "$icc_file" ]; then
        echo "错误: ICC配置文件 $icc_file 未找到"
        echo "请确保ITUR_2100_PQ_FULL.icc文件存在于当前目录"
        exit 1
    fi

    # 使用ImageMagick的HDR效果处理
    if command -v magick &> /dev/null; then
        magick "$input" \
            -colorspace RGB \
            -profile "$icc_file" \
            -define png:include-chunk=all \
            -brightness-contrast 10x20 \
            -sigmoidal-contrast 5,50% \
            -channel RGB -auto-gamma \
            "$output"
    else
        convert "$input" \
            -colorspace RGB \
            -profile "$icc_file" \
            -define png:include-chunk=all \
            -brightness-contrast 10x20 \
            -sigmoidal-contrast 5,50% \
            -channel RGB -auto-gamma \
            "$output"
    fi

    echo "HDR处理完成: $input -> $output"
    # echo "已应用Rec. ITU-R BT.2100 PQ颜色描述文件"
}

# 主函数
main() {
    # 检查参数
    if [[ "$1" == "-h" || "$1" == "--help" ]]; then
        show_help
        return 0
    fi

    if [[ $# -lt 1 || $# -gt 2 ]]; then
        echo "错误: 参数数量不正确"
        show_help
        exit 1
    fi

    check_dependencies

    input_file="$1"

    # 获取输入文件的绝对路径和目录
    input_dir=$(dirname -- "$(realpath -- "$input_file")")
    input_filename=$(basename -- "$input_file")

    # 设置输出文件名
    if [[ $# -eq 2 ]]; then
        output_file="${input_dir}/$(basename -- "$2")"
    else
        # 如果没有指定输出文件名，使用输入文件名加_HDR后缀
        filename="${input_filename%.*}"
        extension="${input_filename##*.}"
        output_file="${input_dir}/${filename}_HDR.${extension}"
    fi

    # 检查输入文件是否存在
    if [[ ! -f "$input_file" ]]; then
        echo "错误: 输入文件不存在: $input_file"
        exit 1
    fi

    # 检查文件扩展名
    if [[ "${input_filename##*.}" != "png" ]]; then
        echo "警告: 输入文件不是PNG格式，但将继续处理"
    fi

    apply_hdr "$input_file" "$output_file"
}

# 执行主函数
main "$@"
