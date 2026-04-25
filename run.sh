#!/bin/bash
# Multi-Resonance-BCI 一键运行脚本

echo "=== Multi-Resonance-BCI 启动 ==="

# 激活虚拟环境
source venv/bin/activate

# 检查依赖是否安装
if ! python -c "import matplotlib" &> /dev/null; then
    echo "正在安装依赖（使用清华镜像）..."
    pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
fi

# 运行仿真
echo "启动闭环仿真..."
cd src/simulation
python main_closed_loop.py
