# 网页交付与本地复核

每组返回 `<clip_id>_r01.zip`，返修递增版本，包含：

- frames/clip_id/000.png 等独立1024²透明RGBA PNG。
- masters/ 原始生成文件，记录真实分辨率。
- manifest.json，参照[模板](templates/submission-manifest.json)。
- prompts.md，记录实际提示词及引用的基准/关键帧。
- qa/web-report.md，实际检查结果及未检查项。
- qa/ 三档播放预览与联系表，不替代PNG。

网页端实际播放100%、50%、25%速度各三轮，记录身份/图标/比例/接触/首尾与透明边缘问题。无法执行或测量必须not_checked/null；不得编造通过。方向图库进行方向扫描与最短路径切换检查。

本地另行执行安全解包、帧号和文件完整性、SHA256、真实格式/Alpha/边距、黑白紫底边缘检查，以及三档播放、关键点对齐、接缝与进出场复核。网页最多标记web_sequence_checked，不能代替本地sequence_checked及runtime_ready。

公开仓库仅提供读取材料，不向网页工具提供GitHub令牌。生成结果通过下载包返回，由本地助手检验后接入。
