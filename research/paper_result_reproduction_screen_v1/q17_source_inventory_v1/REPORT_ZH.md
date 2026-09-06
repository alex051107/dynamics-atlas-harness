# Q17：ChRmine 所需结构和密度图有公开入口

固定作者仓库版本2ea480ff9d7f5fa09443eb927f76b023aa5aebee的7w9w目录包含4个精修PDB，每个559691bytes。EMD-32377官方条目提供主图与两张half-map，元数据均162³网格、0.943182Å像素；三张二进制图和原始/精修坐标尚未下载验收。当前来源页2024-11-13更新，是否与论文运行的历史字节一致仍待核准。

已读来源配置：cc0.8与cc1.0的SCALE分别1.4/1.35，SIGMA_MIN均0.2，体素数据文件与wrap选择也不同。不能把目录之间差异描述为只改噪声权重。作者验证脚本对精修PDB使用原始map与threshold0；论文Figure2所用精确精修版本、残基Voronoi划分、几何原子类型/氢处理仍需接入。

原题可以从已有数据推进，不需要先启动新精修模拟。下一步是核准一个明确的原结构/精修结构配对及相同map/mask，按残基比较局部噪声、拟合和几何。Figure2B的九体系汇总计数不能当作ChRmine单体系正确答案。当前0科学计算、0Rules执行。

来源：[PLUMED-NEST23.041](https://www.plumed-nest.org/eggs/23/041/)；[固定benchmark](https://github.com/COSBlab/EMMIVox-BENCHMARK/tree/2ea480ff9d7f5fa09443eb927f76b023aa5aebee/02-7w9w)；[EMDB官方条目](https://www.ebi.ac.uk/emdb/EMD-32377)。本地receipt保留6个来源文件的Gitblob身份，未运行其安装或模拟命令。
