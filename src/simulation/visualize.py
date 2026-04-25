# src/simulation/visualize.py

import matplotlib.pyplot as plt
import numpy as np

def plot_simulation_results(Rs, fears, I_gvs_history, title="Multi-Resonance-BCI 仿真结果"):
    """绘制仿真结果图表"""
    t = np.arange(len(Rs)) * 0.08  # 时间轴（秒）
    
    plt.figure(figsize=(14, 10))
    
    # 恐惧值
    plt.subplot(3, 1, 1)
    plt.plot(t, fears, 'r-', linewidth=2, label='恐惧水平 (Fear)')
    plt.ylabel('恐惧值 (0-2)')
    plt.title(title)
    plt.grid(True)
    plt.legend()
    
    # 多维 R 值
    plt.subplot(3, 1, 2)
    plt.plot(t, Rs, 'b-', linewidth=2, label='共振率 R')
    plt.axhline(y=6, color='orange', linestyle='--', label='高效共振阈值')
    plt.ylabel('R 值')
    plt.grid(True)
    plt.legend()
    
    # GVS 输出电流
    plt.subplot(3, 1, 3)
    plt.plot(t, I_gvs_history, 'g-', linewidth=2, label='GVS 电流 (mA)')
    plt.xlabel('时间 (秒)')
    plt.ylabel('电流 (mA)')
    plt.grid(True)
    plt.legend()
    
    plt.tight_layout()
    plt.show()


# 如果直接运行此文件，可测试绘图
if __name__ == "__main__":
    print("可视化模块加载完成，可在 main_closed_loop.py 中调用 plot_simulation_results()")
