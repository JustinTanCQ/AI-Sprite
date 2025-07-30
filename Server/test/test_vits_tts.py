import torch
import yaml
import numpy as np
import librosa
import os
import soundfile as sf
from pathlib import Path

# 假设你有一个框架里面的utils.py文件
# 导入框架中的相关方法
from utils import get_model, text_to_feature  # 你需要确保utils.py里面包含这些方法

# Step 1: 加载配置文件
def load_config(config_path):
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    return config

# Step 2: 加载训练好的模型
def load_model(config, model_path):
    model = get_model(config)  # 获取模型结构
    checkpoint = torch.load(model_path)  # 加载模型权重
    model.load_state_dict(checkpoint["state_dict"])  # 加载权重到模型中
    model.eval()  # 设置模型为评估模式
    return model

# Step 3: 文本到声学特征转换
# 在so-vits-svc框架中，通常会使用mel spectrogram作为输入特征
# 这里我们假设 text_to_feature 函数可以根据文本转换为mel spectrogram
def process_text(text, config):
    mel, _, _ = text_to_feature(text, config)  # 将文本转化为mel spectrogram
    mel = torch.FloatTensor(mel).unsqueeze(0)  # 转为Tensor并加上batch维度
    return mel

# Step 4: 执行推理，生成语音
def generate_audio(model, mel):
    with torch.no_grad():  # 禁用梯度计算
        audio = model(mel)  # 将mel spectrogram输入到模型中，生成语音
    return audio

# Step 5: 保存音频
def save_audio(audio, output_path):
    # 将模型输出的音频（通常是波形数据）保存为.wav文件
    audio = audio.squeeze().cpu().numpy()  # 去除多余的维度，并转为numpy数组
    sf.write(output_path, audio, 22050)  # 使用librosa或soundfile保存文件，22050是常见的采样率

# 主函数
def main(config_path, model_path, text, output_audio_path):
    # 加载配置文件
    config = load_config(config_path)
    
    # 加载模型
    model = load_model(config, model_path)
    
    # 处理输入文本
    mel = process_text(text, config)
    
    # 生成音频
    audio = generate_audio(model, mel)
    
    # 保存音频
    save_audio(audio, output_audio_path)
    print(f"生成的音频已保存为 {output_audio_path}")

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(current_dir, "TTS/tp", "config.json")
    model_path = os.path.join(current_dir, "TTS/tp", "G_18500.pth")
    text = "Hello, this is a voice sample"  # 输入的文本
    output_audio_path = "output_audio.wav"  # 输出音频文件路径
    
    # 执行推理并保存音频
    main(config_path, model_path, text, output_audio_path)