# 霜序高清桌宠：网页生图资料

## 新会话自动续接

每次新网页会话复制同一份 [SESSION-PROMPT.md](SESSION-PROMPT.md)。会话按[持续制作协议](CONTINUE.md)读取[进度](progress/state.json)、[队列](progress/QUEUE.json)及未合并生产PR，自动选择下一项。实际图片逐小段提交到web/分支，不等待整套完成；网页检查与本地验收分开，main由复核后合并。

本仓库用于角色高清素材的分组制作、返修和验证。图片可通过GitHub或raw链接公开读取；不代表网页模型必然能够联网浏览或下载图片。

- [动作组索引](GROUPS.md)
- [统一制作规范 V3](STANDARD.md)
- [网页沟通提示词](WEB-PROMPT.md)
- [高清主基准（标准画布）](reference/master_front_1024.png)
- [高清主基准母版](reference/master_front_original.png)
- [全部471份选定母版与标准图索引](assets/catalog.json)
- [辅助素材对应表：33项有来源，3项校准图待制作](reference/auxiliary-coverage.json)
- [完整1512项制作计划](plans/full-plan-v3.jsonl)
- [更正与接触校正规则](CORRECTIONS.md)
- [网页交付与本地检查](RETURN-CHECKLIST.md)
- [完整性复核记录](AUDIT.json)

复核补充：全部471份选定母版与对应标准图已收录，哈希与本地导出记录逐项一致；54组时间线中的文件均存在。增加461份选定新增来源的原提示词、质量检查记录、缺口统计与交付模板。首批10张的基准要求使用STANDARD及组内指令，未伪造缺失的原始提示词。废稿与私人生产日志不属于公开参考。

## 当前状态

2026-10-19工作记录：1509项生图任务中609项有候选来源，900项缺来源；471张来源完成统一导出。17个动画组加64方向图库候选齐全，完整动画正式验收0段。运行桌宠仅试用高清待机、眨眼、视线，其余动作尚未全部高清替换。

本仓库按54组提供已有候选PNG、计划、当前时间线与联系表。来源复用明确记录，不能把PNG数量或帧位覆盖等同于独立绘制数量与验收通过数量。下一步目标是完成所有动作高清素材，经网页组内验证和本地复核后分批接入。

## 每组文件

`groups/<clip_id>/PROMPT.md`：本组要求和验收。

`groups/<clip_id>/planned-frames.jsonl`：各帧计划。

`groups/<clip_id>/current-timeline.json`：已有来源、缺帧、时长与图像路径。

`groups/<clip_id>/current-contact-sheet.png`：顺序检查图；不能替代独立PNG。

`groups/<clip_id>/images/`：实际候选高清PNG。

使用时间线中file字段查找图片时，路径相对于该动作组目录。例如file为`images/initial/master_front.png`，实际路径为`groups/idle/images/initial/master_front.png`。

## 公开范围

仅公开角色参考、选定候选、动作计划和制作指令；不包含聊天记录、凭据、机器设置、桌宠运行缓存或私人项目文档。

## 来源与权利说明

原角色参考来自 https://github.com/sujiu222/gpt-dragon-girl-pet 。新增候选是本项目的AI辅助高清制作成果。原角色及Codex标志等第三方权利不因本仓库公开而转让；此仓库不额外宣称这些素材获得MIT或其他宽泛许可。使用或分发前请核对原来源和生成工具适用条款。
