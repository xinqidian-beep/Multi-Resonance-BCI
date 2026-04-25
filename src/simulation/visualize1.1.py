# src/simulation/visualize1.1.py

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
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    # 多维 R 值
    plt.subplot(3, 1, 2)
    plt.plot(t, Rs, 'b-', linewidth=2, label='共振率 R')
    plt.axhline(y=6, color='orange', linestyle='--', label='高效共振阈值')
    plt.ylabel('R 值')
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    # GVS 输出电流
    plt.subplot(3, 1, 3)
    plt.plot(t, I_gvs_history, 'g-', linewidth=2, label='GVS 电流 (mA)')
    plt.xlabel('时间 (秒)')
    plt.ylabel('电流 (mA)')
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    plt.tight_layout()
    plt.show()

def plot_detailed_results(Rs, fears, balances, touches, thetas, I_gvs_history, 
                         f_hats=None, b_hats=None, t_hats=None,
                         title="Multi-Resonance-BCI 详细仿真结果"): 
    """绘制详细仿真结果图表（包含所有传感器数据）"""
    t = np.arange(len(Rs)) * 0.08  # 时间轴（秒）
    
    fig, axes = plt.subplots(4, 1, figsize=(14, 12))
    
    # 传感器数据
    axes[0].plot(t, fears, 'r-', linewidth=2, label='恐惧 (Fear)')
    axes[0].plot(t, balances, 'b-', linewidth=2, label='平衡 (Balance)')
    axes[0].plot(t, touches, 'g-', linewidth=2, label='触觉 (Touch)')
    axes[0].plot(t, thetas, 'm-', linewidth=2, label='θ (Theta)')
    axes[0].set_ylabel('传感器值')
    axes[0].set_title(title)
    axes[0].grid(True, alpha=0.3)
    axes[0].legend()
    
    # 多维 R 值
    axes[1].plot(t, Rs, 'b-', linewidth=2, label='共振率 R')
    axes[1].axhline(y=6, color='orange', linestyle='--', label='高效共振阈值')
    axes[1].set_ylabel('R 值')
    axes[1].grid(True, alpha=0.3)
    axes[1].legend()
    
    # 定标后的值（如果有提供）
    if f_hats is not None and b_hats is not None and t_hats is not None:
        axes[2].plot(t, f_hats, 'r-', linewidth=2, label='恐惧 (定标)')
        axes[2].plot(t, b_hats, 'b-', linewidth=2, label='平衡 (定标)')
        axes[2].plot(t, t_hats, 'g-', linewidth=2, label='触觉 (定标)')
        axes[2].set_ylabel('定标值 (±2048)')
        axes[2].grid(True, alpha=0.3)
        axes[2].legend()
    
    # GVS 输出电流
    axes[3].plot(t, I_gvs_history, 'g-', linewidth=2, label='GVS 电流 (mA)')
    axes[3].set_xlabel('时间 (秒)')
    axes[3].set_ylabel('电流 (mA)')
    axes[3].grid(True, alpha=0.3)
    axes[3].legend()
    
    plt.tight_layout()
    plt.show()

# 如果直接运行此文件，可测试绘图
if __name__ == "__main__": 
    print("可视化模块加载完成，可在 main_closed_loop.py 中调用 plot_simulation_results()")
