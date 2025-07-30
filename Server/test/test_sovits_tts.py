import requests
import os

# 设置接口的 URL
url = 'http://44.245.213.142:9880/tts'

# 请求的 payload
payload = {
    "text": "我曾因反抗天庭失败而失去信任，如今以独立姿态游走于正邪之间，既可能成为你的盟友，也可能背叛你。",
    "text_lang": "zh",
    "ref_audio_path": "aorun1.wav",
    "prompt_text": "大哥怕是忘了小妹的能耐。若大哥稍降岩浆火力，缓解烧灼之苦。",
    "prompt_lang": "zh",
    "top_k": 5,
    "top_p": 1,
    "temperature": 0.2,
    "text_split_method": "cut0",
    "batch_size": 1,
    "speed_factor": 0.9,
    "streaming_mode": False,
    "seed": -1,
    "parallel_infer": True,
    "media_type": "wav",                                        # str.(optional) media type of the output audio, support "wav", "raw", "ogg", "aac".
    "repetition_penalty": 1.35,
    "tts_infer_yaml_path": "GPT_SoVITS/configs/tts_infer.yaml"
}

# 发送 POST 请求
response = requests.post(url, json=payload)

# 检查响应
if response.status_code == 200:
    # 如果请求成功，获取音频数据
    audio_data = response.content
    
    # 绝对路径，确保文件保存到指定位置
    output_path = os.path.join(os.getcwd(), "output_audio.wav")
    
    # 保存音频到文件
    with open(output_path, "wb") as f:
        f.write(audio_data)
    
    print(f"音频文件已保存为 {output_path}")
else:
    # 如果请求失败，输出错误信息
    print(f"请求失败，错误信息: {response.json()}")