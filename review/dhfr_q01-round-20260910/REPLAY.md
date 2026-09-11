# DHFR 复跑说明

公开数据 DOI https://doi.org/10.5281/zenodo.7966540 ，清单记录每个URL、大小、SHA256、CC-BY4.0。论文JATS https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10428214/fullTextXML 。作者代码固定提交 eba9948e57f25cec9eb9bdb50cfdb234fc23fffc。

使用任务目录作为TASK_ROOT。运行scripts/download_sources.py（需要inputs/zenodo_7966540.json，可由该记录API取得）；VMD2.0b1 -dispdev text -e scripts/extract_distances.tcl -args TASK_ROOT。原始包装坐标只作历史记录。物理接触用scripts/diagnose_periodic_images.tcl；独立实现核对用scripts/validate_with_vmd_pbctools.tcl；汇总scripts/summarize_mic.py。VMD可执行位置由使用者环境提供，不将个人Mac路径当模型可见路径。

两次历史Agent采用同一agent_run.py：DHFR_Q01 A --image sha256:d99fa29fcffbf7de8dce05abf1c71a7002c39acf8e19276328582a5556c84e29 --task-root TASK_ROOT --budget-usd0.20（实际CLI中--budget-usd与0.20分开）。模型openai/gpt-5.6-luna、medium、无providerfallback。source→/source:ro，独立work→/work:rw，Docker断网、2CPU、4GB。模型凭证只在宿主运行器环境，未传容器。

readiness现已关闭；不要直接重跑付费调用。原始request/tooloutput在runs/*/events.jsonl，调用开销在outputs/paid_usage.jsonl（不上传GitHub）。输出同名runner_stage沿用HSP90运行器字符串，不表示DHFR伪装为HSP90实验，case明确DHFR_Q01。

复现本轮科学结果无需API或任何LLM调用。图表scripts/make_figures.py；PPTscripts/build_deck.cjs；报告渲染复用项目render_report.mjs。数据/模型镜像不公开承诺重新打包，本任务保证模型可见路径没有个人本地地址。
