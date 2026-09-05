# Q09 同方法缓存核验

实际D0_01三donor组、两个标记对，在相同padded_linear_v2策略下，缓存与原函数预测相对差最大7.12e-16，完整有限差分梯度缩放差3.75e-11，目标差6.94e-18。缓存保存未归一化分量，混合后才进行响应与总计数归一化；缓存容量128。

一次冷/热完整梯度各比较，约2.14/2.16倍加速，仅为这一组的局部测量。没有优化调用，不建立全33加速或收敛保证。3项聚焦测试首次2通过、1因NumPy数组布尔判断报错；改为长度判断后仅受影响梯度项重跑通过。实际数据核验随后通过。旧拟合未重复。

详见 receipt.json、prediction_checks.json、gradient_checks.json；实现 q09_cached_group_v2.py，实际 runner scripts/check_q09_cached_group_v2.py。
