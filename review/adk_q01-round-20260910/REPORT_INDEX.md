# ADK：数据准入与方法反例，尚无Agent答复

四文件已下载校验，现有半盒长准入标准不通过；未冻结科学答案、未运行Agent。

[完整科学与项目读本](../one_shot-20260910/report/DEEP_READER_ZH.md) · [GROMACS核对](outputs/GROMACS_GATE_CROSSCHECK.json) · [下载清单](outputs/DOWNLOAD_MANIFEST.json)

原始1.373GB数据、坐标派生表和凭证不入库。scripts使用自身目录确定任务路径；公开Zenodo地址见下载清单。复现需要VMD2.0b1、GROMACS2025.1与Python/numpy。先下载四文件，再在项目根目录运行VMD脚本并传入本任务目录，随后运行派生与核对脚本。旧GROMACS核对JSON保留实际执行命令中的绝对路径；可重跑脚本按当前任务目录生成命令，不依赖原机器路径。
