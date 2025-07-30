import requests
import os
import sys
import time

import logging
logging.getLogger().setLevel(logging.INFO)
logging.basicConfig(level=logging.INFO)

server_url = 'http://10.0.29.129:9880/tts'

class GPTSoVitsService():
    def __init__(self):
        logging.info('Initializing GPTSoVits Service...')
        
    
    def read_save(self, text, filename):
        payload = {
            "text": text,
            "text_lang": "zh",
            "ref_audio_path": "aorun1.wav",
            "prompt_text": "大哥怕是忘了小妹的能耐。若大哥稍降岩浆火力，缓解烧灼之苦。",
            "prompt_lang": "zh",
            "top_k": 5,
            "top_p": 1,
            "temperature": 0.2,
            "text_split_method": "cut3",
            "batch_size": 16,
            "speed_factor": 1,
            "streaming_mode": False,
            "seed": -1,
            "parallel_infer": True,
            "media_type": "wav",                                        # str.(optional) media type of the output audio, support "wav", "raw", "ogg", "aac".
            "repetition_penalty": 1.35,
            "tts_infer_yaml_path": "GPT_SoVITS/configs/tts_infer.yaml"
        }
        stime = time.time()
        
        response = requests.post(server_url, json=payload)

        # 检查响应
        if response.status_code == 200:
            # 如果请求成功，获取音频数据
            audio_data = response.content
            
            # 绝对路径，确保文件保存到指定位置
            output_path = os.path.join(os.getcwd(), "output_audio.wav")
            
            # 保存音频到文件
            with open(filename, "wb") as f:
                f.write(audio_data)
            logging.info('SoVits Done, time used %.2f' % (time.time() - stime))
            
        else:
            # 如果请求失败，输出错误信息
            logging.info(f"Request Error: {response.json()}")