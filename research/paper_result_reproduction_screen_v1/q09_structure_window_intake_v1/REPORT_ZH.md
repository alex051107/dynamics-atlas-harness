# 结构前向输入与窗口定位

172L与148L小型原始坐标已取得并保留。172L的A链、148L的E链是当前蛋白编号检查对象；148L另有单残基S链。所有33对标记涉及的位点均能在两蛋白链找到CA/CB；这只是位点完整性，不是染料距离预测。

实际源清单、sha256、链/位点与header在structures.json；原PDB保存在任务inputs/q09_structures。没有将PDB原始资料重新发布。

论文ACV方法需要染料连接几何、靠表面的接触层及各位点各染料的残余/基本各向异性。已定位的程序mdtraj_fps依赖MDTraj和原FPS二进制，当前环境均未安装；无依赖安装授权，未安装或执行新程序。染料结构预测0项，具体缺口在dye_forward_method_admission.json。

参考：[论文方法](https://www.nature.com/articles/s41467-020-14886-w)、[作者工具仓库](https://github.com/Fluorescence-Tools/mdtraj_fps)、[172L](https://www.rcsb.org/structure/172L)、[148L](https://www.rcsb.org/structure/148L)。源匹配Markdown只用于检索；其双栏顺序混乱处未被用来编码密度公式。

两条D0参考的窗口排除均发生于首段约0–3.4ns，分别2170/946光子，占0.0066%左右；尾端排除段为0光子。未作纯背景判断、未改mask。详见window_exclusions.json。
