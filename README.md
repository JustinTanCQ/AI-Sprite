# AI-Sprite

## 🎭 项目简介

AI-Sprite 是一个基于大语言模型和语音合成技术的智能角色扮演系统，能够创建具有独特个性和声音的AI虚拟角色。该项目结合了先进的自然语言处理、情感分析和语音克隆技术，为用户提供沉浸式的角色互动体验。

### ✨ 核心特性

🎪 **角色扮演系统**
- 支持多种预设角色（纳西妲、派蒙、奥伦等原神角色）
- 每个角色都有独特的性格设定和对话风格
- 基于角色背景的个性化回复生成

🔊 **语音克隆技术**
- 集成 GPT-SoVITS 高质量语音合成引擎
- 支持角色专属语音克隆，还原角色独特音色
- 实时文本转语音，提供自然流畅的语音输出

🧠 **智能对话引擎**
- 基于大语言模型的自然对话能力
- 上下文感知，支持连续对话
- 角色一致性保持，确保对话符合角色设定

😊 **情感分析系统**
- 实时分析用户输入的情感状态
- 支持6种情感识别：开心、害怕、生气、失落、好奇、调侃
- 基于情感状态调整角色回复风格

🎤 **语音识别功能**
- 实时语音转文本
- 支持中文语音识别
- 流式处理，低延迟响应

### 🎬 项目演示

#### 演示视频

**原神角色演示（纳西妲 & 派蒙）**

![原神角色演示](Demo/demo-yuanshen.mp4)

**哪吒角色演示（敖润）**

![哪吒角色演示](Demo/demo-aurun.mp4)

*演示视频展示了AI-Sprite的完整交互流程：语音输入 → 语音识别 → 情感分析 → 角色对话生成 → 语音合成输出*

### 🏗️ 技术架构

- **ASR模块**: 基于 Paraformer 的自动语音识别
- **LLM模块**: 大语言模型驱动的对话生成
- **TTS模块**: GPT-SoVITS 语音合成引擎
- **情感引擎**: 基于BERT的情感分析模型
- **WebSocket服务**: 实时通信支持

---

Use LLM and TTS to make your own AI Sprites.

## 安装和运行指南

### 环境要求
- Python 3.10+
- macOS (推荐) 或其他支持的操作系统

### 安装步骤

1. **克隆项目**
   ```bash
   git clone <repository-url>
   cd AI-Sprite
   ```

2. **创建虚拟环境**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # macOS/Linux
   # 或者在Windows上: venv\Scripts\activate
   ```

3. **升级pip**
   ```bash
   pip install --upgrade pip
   ```

4. **安装依赖包**
   ```bash
   pip install -r requirements.txt
   ```

   如果遇到SSL错误，可以使用以下命令：
   ```bash
   pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -r requirements.txt
   ```

5. **安装系统依赖**
   
   **macOS:**
   ```bash
   brew install portaudio
   ```
   
   **Amazon Linux / CentOS / RHEL:**
   ```bash
   # 更新系统包
   sudo yum update -y
   
   # 安装开发工具和依赖
   sudo yum groupinstall -y "Development Tools"
   sudo yum install -y python3 python3-pip python3-devel
   
   # 安装音频处理依赖
   sudo yum install -y portaudio-devel alsa-lib-devel
   
   # 安装其他系统依赖
   sudo yum install -y gcc gcc-c++ make cmake
   sudo yum install -y libffi-devel openssl-devel
   ```
   
   **Ubuntu/Debian:**
   ```bash
   sudo apt-get update
   sudo apt-get install -y python3 python3-pip python3-venv python3-dev
   sudo apt-get install -y portaudio19-dev libasound2-dev
   sudo apt-get install -y build-essential cmake
   sudo apt-get install -y libffi-dev libssl-dev
   ```

### Amazon Linux 完整安装示例

如果你在Amazon Linux上运行，可以使用以下完整的安装脚本：

```bash
# 1. 更新系统并安装基础依赖
sudo yum update -y
sudo yum groupinstall -y "Development Tools"
sudo yum install -y python3 python3-pip python3-devel
sudo yum install -y portaudio-devel alsa-lib-devel
sudo yum install -y gcc gcc-c++ make cmake
sudo yum install -y libffi-devel openssl-devel

# 2. 克隆项目
git clone <repository-url>
cd AI-Sprite

# 3. 创建虚拟环境
python3 -m venv venv
source venv/bin/activate

# 4. 升级pip
pip install --upgrade pip

# 5. 安装Python依赖
pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -r requirements.txt

# 如果网络较慢，可以分步安装核心依赖
# pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org numpy scipy librosa
# pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org transformers torch onnxruntime

# 6. 运行项目
cd Server
python run_script.py
```

### 运行项目

1. **激活虚拟环境**
   ```bash
   source venv/bin/activate
   ```

2. **运行服务器**
   ```bash
   cd Server
   python run_script.py
   ```

   或者直接运行：
   ```bash
   cd Server
   python SocketServer.py --stream False --character aorun
   ```

## GPT-SoVITS 安装和配置

### GPT-SoVITS 简介
GPT-SoVITS 是本项目使用的文本转语音(TTS)引擎，提供高质量的语音合成功能。

### 安装方法
请参考官方文档进行安装：
**[GPT-SoVITS fast_inference 分支](https://github.com/RVC-Boss/GPT-SoVITS/tree/fast_inference_)**

⚠️ **重要提醒**：请务必使用 `fast_inference_` 分支，只有这个分支才包含本项目所需的 `api_v3` 接口。

### 部署建议

#### 方案1：同服务器部署（适合测试）
- GPT-SoVITS 和 AI-Sprite 主服务器部署在同一台机器上
- 优点：配置简单，音频传输速度快
- 缺点：资源竞争，性能可能受影响

#### 方案2：独立服务器部署（推荐生产环境）
- GPT-SoVITS 部署在独立的服务器上
- 建议通过内网连接，确保音频传输速率
- 优点：性能更好，资源隔离
- 缺点：需要额外的服务器资源

### 配置连接地址

在你的配置中设置 GPT-SoVITS 服务地址：

```python
# 示例配置
server_url = 'http://10.0.29.129:9880/tts'
```

**地址配置说明**：
- **本机部署**：`http://localhost:9880/tts` 或 `http://127.0.0.1:9880/tts`
- **内网部署**：`http://内网IP:9880/tts`（如示例中的 `http://10.0.29.129:9880/tts`）
- **公网部署**：`http://公网IP:9880/tts`（不推荐，安全性和速度都不理想）

💡 **配置参考**：可以查看 `Server/config_example.py` 文件了解详细的配置选项。

### 性能优化建议

1. **网络优化**：
   - 优先使用内网连接
   - 确保网络带宽充足
   - 避免跨地域部署

2. **服务器配置**：
   - GPT-SoVITS 建议使用GPU加速
   - 确保有足够的内存和存储空间
   - 监控服务状态和性能指标

### 项目结构
```
AI-Sprite/
├── Server/           # 服务器端代码
│   ├── ASR/         # 自动语音识别模块
│   ├── LLM/         # 大语言模型模块
│   ├── TTS/         # 文本转语音模块
│   ├── SentimentEngine/  # 情感分析引擎
│   │   ├── SentimentEngine.py  # 情感分析主类
│   │   └── models/             # ONNX模型文件
│   ├── utils/       # 工具函数
│   ├── SocketServer.py   # 主服务器文件
│   └── run_script.py     # 启动脚本
├── Web/             # 前端代码
└── requirements.txt # Python依赖包列表
```

### 功能模块说明

- **ASR (自动语音识别)**：将语音转换为文本
- **LLM (大语言模型)**：处理自然语言对话
- **TTS (文本转语音)**：将文本转换为语音
- **SentimentEngine (情感分析)**：分析文本情感，支持6种情感类型：
  - 0: 开心
  - 1: 害怕  
  - 2: 生气
  - 3: 失落
  - 4: 好奇
  - 5: 调侃

### 故障排除

1. **SSL证书错误**
   - 使用 `--trusted-host` 参数安装包
   - 或者更新证书：`pip install --upgrade certifi`

2. **缺少系统依赖**
   - macOS: `brew install portaudio`
   - Amazon Linux: `sudo yum install -y portaudio-devel alsa-lib-devel`
   - Ubuntu: `sudo apt-get install portaudio19-dev`

3. **Python版本问题**
   - 确保使用Python 3.10或更高版本
   - 使用 `python3` 而不是 `python` 命令
   - Amazon Linux上可能需要安装更新的Python版本：
     ```bash
     sudo yum install -y python3.10 python3.10-pip python3.10-devel
     ```

4. **编译错误 (Amazon Linux)**
   - 确保安装了开发工具：
     ```bash
     sudo yum groupinstall -y "Development Tools"
     sudo yum install -y gcc gcc-c++ make cmake
     ```
   - 如果遇到LLVM相关错误，可能需要安装特定版本的LLVM：
     ```bash
     sudo yum install -y llvm-devel
     ```

5. **音频设备问题**
   - 在无头服务器环境中，可能需要配置虚拟音频设备
   - Amazon Linux上可以安装pulseaudio：
     ```bash
     sudo yum install -y pulseaudio pulseaudio-utils
     ```

6. **权限问题**
   - 确保用户有权限访问音频设备
   - 可能需要将用户添加到audio组：
     ```bash
     sudo usermod -a -G audio $USER
     ```

7. **情感分析模块问题**
   - 如果遇到 `transformers` 相关错误，确保安装了正确版本：
     ```bash
     pip install transformers>=4.20.0 torch>=1.9.0
     ```
   - 首次运行时会自动下载BERT模型，需要网络连接
   - 如果下载失败，可以手动设置镜像：
     ```bash
     export HF_ENDPOINT=https://hf-mirror.com
     ```

8. **测试各个模块**
   - 测试情感分析模块：
     ```bash
     cd Server
     python test_sentiment.py
     ```

### 配置说明

#### 使用 run_script.py (推荐)

`run_script.py` 是一个配置脚本，让你可以在一个地方设置所有参数，然后直接运行：

1. **编辑配置**：打开 `Server/run_script.py`，修改配置区域的参数：
   ```python
   # 基本配置
   STREAM = "False"          # 是否启用流式处理: True/False
   CHARACTER = "aorun"       # 角色名称
   
   # 可选配置
   PROXY = None              # 代理设置
   IP = None                 # IP地址
   BRAINWASH = None          # 是否启用brainwash: True/False
   ```

2. **运行服务器**：
   ```bash
   cd Server
   python run_script.py
   ```

#### 直接运行 SocketServer.py

如果你想直接运行主服务器文件，需要手动指定参数：

```bash
python SocketServer.py --stream False --character aorun
```

支持的参数：
- `--stream`: 是否启用流式处理 (True/False) - **必需**
- `--character`: 角色名称 - **必需**
- `--proxy`: 代理设置 - 可选
- `--ip`: IP地址 - 可选
- `--brainwash`: 是否启用brainwash (True/False) - 可选

示例：
```bash
python SocketServer.py --stream True --character custom_character --ip 192.168.1.100
```
