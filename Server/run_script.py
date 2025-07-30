import subprocess
import sys

# ==================== 配置区域 ====================
# 在这里修改你的配置，然后直接运行 python run_script.py

# 基本配置
SCRIPT_NAME = "SocketServer.py"
STREAM = "False"          # 是否启用流式处理: True/False
CHARACTER = "aorun"       # 角色名称

# 可选配置 (设置为 None 表示不使用该参数)
PROXY = None              # 代理设置
IP = None                 # IP地址
BRAINWASH = None          # 是否启用brainwash: True/False

# ==================== 自动构建命令 ====================

def build_command():
    """根据配置构建命令行参数"""
    command = ["python3", SCRIPT_NAME]
    
    # 必需参数
    command.extend(["--stream", STREAM])
    command.extend(["--character", CHARACTER])
    
    # 可选参数
    if PROXY is not None:
        command.extend(["--proxy", PROXY])
    if IP is not None:
        command.extend(["--ip", IP])
    if BRAINWASH is not None:
        command.extend(["--brainwash", str(BRAINWASH)])
    
    return command

def main():
    """主函数"""
    command = build_command()
    
    print("=" * 50)
    print("AI-Sprite 服务器启动脚本")
    print("=" * 50)
    print(f"执行命令: {' '.join(command)}")
    print("=" * 50)
    print("配置信息:")
    print(f"  流式处理: {STREAM}")
    print(f"  角色名称: {CHARACTER}")
    if PROXY: print(f"  代理设置: {PROXY}")
    if IP: print(f"  IP地址: {IP}")
    if BRAINWASH: print(f"  Brainwash: {BRAINWASH}")
    print("=" * 50)
    print("正在启动服务器...")
    print()
    
    try:
        # 运行命令
        subprocess.run(command)
    except KeyboardInterrupt:
        print("\n服务器已停止")
    except Exception as e:
        print(f"启动失败: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
