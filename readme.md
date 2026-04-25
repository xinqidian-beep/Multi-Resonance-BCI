# Multi-Resonance-BCI

**多维共振率闭环神经调控框架**  
*(Multi-dimensional Resonance Rate Closed-Loop Framework)*

一个理论驱动的 BCI 系统，专注于 VR / 恐怖游戏中的**情绪与感知自适应调控**。

### 核心创新
- **多维共振率 R**：将恐惧、平衡感、触感等信号建模为共振系统
- **±2048 整数定标 + Q11.0 定点数**：彻底消除浮点长期累积误差
- 支持**自组织闭环**，实现“又怕又爽、可控沉浸”的玩家体验

### 项目状态
- [x] 理论框架与数学推导
- [x] 整数定标优化
- [x] 仿真代码与可视化
- [ ] 硬件原型
- [ ] 人体实验验证

### 快速导航
- [理论框架](./docs/01_理论框架.md)
- [整数定标方案](./docs/02_整数定标方案.md)
- [玩家体验推演](./docs/03_玩家体验推演.md)
- [仿真代码](./src/simulation/)
- [论文草稿](./papers/) （后续添加）

### 如何运行仿真
```bash
cd src/simulation
pip install -r ../../requirements.txt
python main_closed_loop.py

欢迎共建！
理论研究者、BCI 工程师、VR 开发者均可提交 Issue / PR。


---

#### 2. 新建 `requirements.txt`（仓库根目录）

**文件名**：`requirements.txt`

```txt
matplotlib>=3.8.0
numpy>=1.26.0
