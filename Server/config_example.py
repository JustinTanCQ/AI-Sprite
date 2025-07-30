#!/usr/bin/env python3
"""
GPT-SoVITS 配置示例

请根据你的部署情况修改以下配置
"""

# GPT-SoVITS 服务器配置
class GPTSoVITSConfig:
    # 服务器地址配置
    # 根据你的部署方式选择合适的地址
    
    # 方案1: 本机部署
    # server_url = 'http://localhost:9880/tts'
    # server_url = 'http://127.0.0.1:9880/tts'
    
    # 方案2: 内网部署（推荐）
    server_url = 'http://10.0.29.129:9880/tts'
    
    # 方案3: 公网部署（不推荐）
    # server_url = 'http://your-public-ip:9880/tts'
    
    # 其他配置
    timeout = 30  # 请求超时时间（秒）
    retry_times = 3  # 重试次数

# 使用示例
if __name__ == '__main__':
    config = GPTSoVITSConfig()
    print(f"GPT-SoVITS 服务地址: {config.server_url}")
    print(f"超时时间: {config.timeout}秒")
    print(f"重试次数: {config.retry_times}次")
