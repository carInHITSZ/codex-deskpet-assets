# 可复制到网页端的提示词

跨新会话自动续接全部动作请改用 [SESSION-PROMPT.md](SESSION-PROMPT.md) 与 [CONTINUE.md](CONTINUE.md)。以下保留为单组手动任务模式；指定idle不是自动队列的固定起点。

将下面的 `idle` 改成目标动作组标识；第一次建议使用idle。若网页工具无法联网读图，GitHub公开并不能绕过这个能力限制，请改为只上传主基准和相邻关键帧。

```text
请协助完成霜序桌面龙娘的高清动画，本次只处理动作组：idle。

公开资料仓库：
https://github.com/carInHITSZ/codex-deskpet-assets

请先实际访问以下资料，不要只根据链接名称推测内容。规范优先级：CORRECTIONS及具体更正记录 > STANDARD V3 > 本组指令 > 历史计划。
规范：https://raw.githubusercontent.com/carInHITSZ/codex-deskpet-assets/main/STANDARD.md
动作索引：https://raw.githubusercontent.com/carInHITSZ/codex-deskpet-assets/main/GROUPS.md
本组指令：https://raw.githubusercontent.com/carInHITSZ/codex-deskpet-assets/main/groups/idle/PROMPT.md
本组计划：https://raw.githubusercontent.com/carInHITSZ/codex-deskpet-assets/main/groups/idle/planned-frames.jsonl
本组时间线：https://raw.githubusercontent.com/carInHITSZ/codex-deskpet-assets/main/groups/idle/current-timeline.json
角色主基准：https://raw.githubusercontent.com/carInHITSZ/codex-deskpet-assets/main/reference/master_front_1024.png
生成母版：https://raw.githubusercontent.com/carInHITSZ/codex-deskpet-assets/main/reference/master_front_original.png
完整性核对：https://raw.githubusercontent.com/carInHITSZ/codex-deskpet-assets/main/AUDIT.json
更正规则：https://raw.githubusercontent.com/carInHITSZ/codex-deskpet-assets/main/CORRECTIONS.md
选定资产与母版索引：https://raw.githubusercontent.com/carInHITSZ/codex-deskpet-assets/main/assets/catalog.json
辅助参考：https://raw.githubusercontent.com/carInHITSZ/codex-deskpet-assets/main/reference/auxiliary-coverage.json
质量与缺口记录：https://github.com/carInHITSZ/codex-deskpet-assets/tree/main/qa
交付要求：https://raw.githubusercontent.com/carInHITSZ/codex-deskpet-assets/main/RETURN-CHECKLIST.md
交付模板：https://raw.githubusercontent.com/carInHITSZ/codex-deskpet-assets/main/templates/submission-manifest.json
失落抱膝更正：https://raw.githubusercontent.com/carInHITSZ/codex-deskpet-assets/main/corrections/failed-motion-correction.json

先报告实际读取结果、本组已有候选数量、缺帧号和需返修项。
时间线中的file相对于groups/idle/目录。按该路径读取真实PNG，联系表不能代替逐帧参考。资产索引路径相对仓库根目录，按本组需要读取多视图、手部、表情、道具或翼结构，不一次下载全库。计划目标路径不代表已交付文件；3项程序校准图仍无来源。先读取对应qa记录，针对已知问题返修。
如果不能联网访问图片、不能将下载图片用作生图参考，立即说明并列出需要我手动上传的最少文件，不能声称已经看过。

V3规范优先。全部输出高清重绘，保持唯一角色基准：白发紫瞳、两角两翼一尾、原白紫服饰；头侧挂饰必须是Codex交织图标，绝不是花朵。
先验证关键姿态，再补中间帧。保留合格候选，定向返修尺度/脸型/挂饰/接触漂移，不用复制图片凑帧数，不用透明叠化伪造动作。

最终独立PNG为1024×1024、8-bit RGBA、真实Alpha；站姿锚点[512,896]，基准角尖到脚底640px，主体边距至少24px。不同姿态保持身体比例，不逐帧按外框缩放。保留原始生成母版，记录实际尺寸。

素材齐全后实际组装动画，在100%、50%、25%速度下各检查三轮。检查接触滑动、比例闪跳、身份/图标变化、重复缺帧、循环接缝、进入退出和透明边缘。方向图库改用方向扫描及最短角切换验证。
没有实际执行的项目标not_checked；禁止伪造播放、测量或验收记录。网页验证通过仅标web_sequence_checked，本地检测后才考虑runtime_ready。

交付<clip_id>_r01.zip，内含：frames/<clip_id>/000.png等独立帧、masters原稿、manifest.json、prompts.md、qa/web-report.md及实际三档播放预览。manifest记录帧序、durationMs、来源复用、实际尺寸、锚点、接触点及motionOwner；未知值null。
不能只交联系表/GIF/视频。若无法生成可下载ZIP，交付原始PNG下载及对应manifest，不用聊天截图代替原图。

请先读取并检查资料，然后开始本组制作。不要同时制作所有54组。
```
