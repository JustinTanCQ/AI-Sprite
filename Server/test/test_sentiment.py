#!/usr/bin/env python3
"""
测试SentimentEngine导入和初始化
"""

try:
    print("正在测试SentimentEngine导入...")
    from SentimentEngine import SentimentEngine
    print("✓ SentimentEngine导入成功")
    
    print("正在测试SentimentEngine初始化...")
    sentiment = SentimentEngine('SentimentEngine/models/sentiment.onnx')
    print("✓ SentimentEngine初始化成功")
    
    print("正在测试情感分析...")
    result = sentiment.infer("今天天气真好！")
    print(f"✓ 情感分析测试成功，结果: {result}")
    print("情感标签: 0=开心 1=害怕 2=生气 3=失落 4=好奇 5=调侃")
    
except ImportError as e:
    print(f"✗ 导入错误: {e}")
    print("请确保已安装所需依赖: pip install transformers torch onnxruntime")
except Exception as e:
    print(f"✗ 其他错误: {e}")
    import traceback
    traceback.print_exc()
