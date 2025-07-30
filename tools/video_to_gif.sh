#!/bin/bash
# 视频转GIF工具脚本
# 使用方法: ./video_to_gif.sh input.mp4 output.gif

if [ $# -ne 2 ]; then
    echo "使用方法: $0 <输入视频> <输出GIF>"
    echo "示例: $0 demo.mp4 demo.gif"
    exit 1
fi

INPUT_VIDEO="$1"
OUTPUT_GIF="$2"

# 检查输入文件是否存在
if [ ! -f "$INPUT_VIDEO" ]; then
    echo "错误: 输入文件 '$INPUT_VIDEO' 不存在"
    exit 1
fi

# 检查是否安装了ffmpeg
if ! command -v ffmpeg &> /dev/null; then
    echo "错误: 未找到ffmpeg，请先安装ffmpeg"
    echo "macOS: brew install ffmpeg"
    echo "Ubuntu: sudo apt-get install ffmpeg"
    echo "Amazon Linux: sudo yum install ffmpeg"
    exit 1
fi

echo "正在转换视频到GIF..."
echo "输入文件: $INPUT_VIDEO"
echo "输出文件: $OUTPUT_GIF"

# 转换参数说明:
# fps=10: 设置帧率为10fps（降低文件大小）
# scale=640:-1: 宽度设为640px，高度自动计算保持比例
# -t 30: 只转换前30秒（可选）

ffmpeg -i "$INPUT_VIDEO" \
    -vf "fps=10,scale=640:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" \
    -loop 0 \
    "$OUTPUT_GIF"

if [ $? -eq 0 ]; then
    echo "✓ 转换成功!"
    echo "输出文件: $OUTPUT_GIF"
    
    # 显示文件大小
    if command -v du &> /dev/null; then
        SIZE=$(du -h "$OUTPUT_GIF" | cut -f1)
        echo "文件大小: $SIZE"
        
        # 如果文件太大，给出建议
        SIZE_BYTES=$(du -b "$OUTPUT_GIF" | cut -f1)
        if [ "$SIZE_BYTES" -gt 10485760 ]; then  # 10MB
            echo "⚠️  警告: 文件大小超过10MB，建议进一步压缩"
            echo "建议: 降低分辨率或帧率"
        fi
    fi
else
    echo "✗ 转换失败"
    exit 1
fi
