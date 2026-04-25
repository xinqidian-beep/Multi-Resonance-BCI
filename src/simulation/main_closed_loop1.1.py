# -*- coding:  utf-8 -*-
"""
Multi-Resonance-BCI 仿真主程序1.1
±2048 整数定标 + 多维 R 闭环演示
"""

import math
import time
import matplotlib.pyplot as plt
from collections import deque
import random

# ====================== 参数配置 ======================
FS = 12.5                    # 采样率 (80ms = 12.5Hz)
WINDOW = 20                  # 滑动窗长度 (~1.6秒)
S = 2048                     # 定标因子 ±2048
DEADZONE = 0.3

# 中值
MID = {'fear':  1.0,  'balance':  1.0,  'touch':  1.0,  'theta':  7.0}

# ====================== 仿真数据生成 ======================
def generate_sensor_data(t): 
    """模拟真实生理信号"""
    fear = 1.0 + 0.8 * math.sin(t * 3) + 0.3 * math.sin(t * 12)
    balance = 1.0 + 0.6 * math.sin(t * 2.5) + 0.4 * math.cos(t * 8)
    touch = 1.0 + 0.5 * math.sin(t * 4)
    theta = 7.0 + 2.0 * math.sin(t * 3.5)
    
    # 加入随机噪声
    fear += random.gauss(0,  0.15)
    balance += random.gauss(0,  0.12)
    touch += random.gauss(0,  0.1)
    
    return max(0.2,  min(2.0,  fear)),  max(0.2,  min(2.0,  balance)),  max(0.2,  min(2.0,  touch)),  theta

# ====================== 多维 R 计算（整数定标版） ======================
def compute_resonance(fear,  balance,  touch,  theta): 
    # 1. 中值零化
    f_til = fear - MID['fear']
    b_til = balance - MID['balance']
    t_til = touch - MID['touch']
    th_til = theta - MID['theta']
    
    # 2. 死区滤波
    if abs(f_til) < DEADZONE:  f_til = 0
    if abs(b_til) < DEADZONE:  b_til = 0
    if abs(t_til) < DEADZONE:  t_til = 0
    
    # 3. ±2048 定标
    f_hat = max(-S,  min(S,  int(f_til * S)))
    b_hat = max(-S,  min(S,  int(b_til * S)))
    t_hat = max(-S,  min(S,  int(t_til * S)))
    
    # 简化版 R 计算（演示用）
    v = 1 + abs(f_hat) / S
    lift = int(0.8 * (0.6 * f_hat + 0.4 * b_hat) * v * v)
    circ = int(1.0 * v * (f_hat + b_hat + t_hat))
    phi = int(1024 * math.exp(-0.15 * abs(7.0 - theta)))  # 定点近似
    
    numer = lift + circ
    denom = 500 + abs(f_hat)//4 + abs(b_hat)//4 + 10  # 模拟分母
    R = numer / denom if denom > 0 else 1.0
    
    return R,  f_hat,  b_hat,  t_hat

# ====================== 主闭环 ======================
print("Multi-Resonance-BCI 仿真启动... (Ctrl+C 停止)")

Rs = []
fears = []
I_gvs_history = []
I_gvs = 0.5

try: 
    for step in range(300):           # 模拟 24 秒
        t = step / FS
        fear,  balance,  touch,  theta = generate_sensor_data(t)
        
        R,  _,  _,  _ = compute_resonance(fear,  balance,  touch,  theta)
        
        # 自适应控制
        Kp = 0.25 * (0.5 + 0.5 * (R / 8.0))
        I_gvs = 0.5 - Kp * (fear - 1.0)
        I_gvs = max(0.0,  min(1.0,  I_gvs))
        
        Rs.append(R)
        fears.append(fear)
        I_gvs_history.append(I_gvs)
        
        if step % 25 == 0: 
            print(f"Step {step: 3d} | Fear:  {fear: .2f} | R:  {R: .2f} | GVS:  {I_gvs: .3f} mA")
        
        time.sleep(0.08)
        
except KeyboardInterrupt: 
    print("\n仿真停止")

# ====================== 绘图 ======================
plt.figure(figsize=(12,  8))
plt.subplot(3, 1, 1)
plt.plot(fears,  label='Fear Level',  color='red')
plt.ylabel('Fear')
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(Rs,  label='Resonance Rate R',  color='blue')
plt.ylabel('R Value')
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(I_gvs_history,  label='GVS Current',  color='green')
plt.xlabel('Time Step (80ms)')
plt.ylabel('GVS (mA)')
plt.legend()

plt.suptitle('Multi-Resonance-BCI 闭环仿真结果 (±2048 定标)')
plt.tight_layout()
plt.show()
