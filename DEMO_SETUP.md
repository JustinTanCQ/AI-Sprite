# 演示文件设置指南

## 推荐的演示文件结构

```
AI-Sprite/
├── demo/                    # 演示文件夹
│   ├── ai-sprite-demo.mp4   # 主要演示视频
│   ├── ai-sprite-demo.gif   # 演示动图（推荐）
│   └── features/            # 功能演示
│       ├── asr-demo.gif     # 语音识别演示
│       ├── llm-demo.gif     # 对话演示
│       ├── tts-demo.gif     # 语音合成演示
│       └── sentiment-demo.gif # 情感分析演示
├── screenshots/             # 截图文件夹
│   ├── main-interface.png   # 主界面截图
│   ├── config-panel.png     # 配置面板
│   └── running-status.png   # 运行状态
└── README.md
```

## 视频添加方法

### 1. 直接上传视频文件（推荐）
1. 将视频文件放在 `demo/` 目录下
2. 在README中使用：
   ```markdown
   ![AI-Sprite演示](demo/ai-sprite-demo.mp4)
   ```

### 2. 使用GIF动图（兼容性最好）
1. 将视频转换为GIF格式
2. 文件大小建议控制在10MB以内
3. 在README中使用：
   ```markdown
   ![AI-Sprite演示](demo/ai-sprite-demo.gif)
   ```

### 3. 外部视频链接
#### YouTube视频：
```markdown
[![AI-Sprite演示](https://img.youtube.com/vi/YOUR_VIDEO_ID/0.jpg)](https://www.youtube.com/watch?v=YOUR_VIDEO_ID)
```

#### B站视频：
```markdown
📺 **演示视频**：[点击观看B站演示视频](https://www.bilibili.com/video/BV1234567890)
```

## 视频制作建议

### 内容建议：
1. **项目介绍** (30秒)
   - 项目名称和主要功能
   - 技术栈简介

2. **功能演示** (2-3分钟)
   - 语音输入演示
   - 实时语音识别
   - LLM对话生成
   - 情感分析结果
   - TTS语音输出

3. **配置展示** (1分钟)
   - 配置文件设置
   - 不同角色切换
   - 参数调整效果

### 技术要求：
- **分辨率**：1920x1080 或 1280x720
- **格式**：MP4 (H.264编码)
- **时长**：建议3-5分钟
- **文件大小**：GitHub单文件限制100MB

### GIF制作工具：
- **FFmpeg**：`ffmpeg -i input.mp4 -vf "fps=10,scale=640:-1" output.gif`
- **在线工具**：ezgif.com, giphy.com
- **桌面工具**：ScreenToGif, LICEcap

## 截图建议

### 主要截图：
1. **主界面**：显示完整的用户界面
2. **配置面板**：展示配置选项
3. **运行状态**：显示实时处理过程
4. **结果展示**：显示输出结果

### 截图规范：
- **格式**：PNG（支持透明背景）
- **分辨率**：保持原始分辨率
- **命名**：使用描述性文件名
- **大小**：单个文件建议小于5MB
