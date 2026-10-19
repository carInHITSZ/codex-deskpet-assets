# blink r01 — 起始QA报告（待CI结果）

先对17帧位/9个唯一候选源独立解码，生成真实三背景与眼睑/挂饰局部对照；Chrome实际绘制100%、50%、25%各3次。不修改源图，不将反向重复帧称为新绘。CI未完成前不得宣称成功。

当前正式验收新绘数0；眼睑自然性、角色身份、双足解剖接触、关键点尺度、idle→blink进入退出与本地桌宠均未检查。

## 2026-10-19T10:43:43.151Z — 远端实测与本轮源图复核（无生产PNG提交）

- **源技术测试完成**：[GitHub Actions #39239051047](https://github.com/carInHITSZ/codex-deskpet-assets/actions/runs/39239051047)、[17帧源图技术审计](source-audit.json)。17帧均为PNG 1024×1024 8-bit RGBA，边距≥24px，真实Alpha。共有9个唯一实际源，回程逆序复用，首末源哈希严格相同。
- **浏览器实际播放完成**：[Chrome记录](browser-playback.json)：100% 2.1244s/三次、50% 4.2497s/三次、25% 8.4996s/三次；每档3遍17帧=51帧真实canvas绘制，序列无误，pageerror 0。这是机械完成，非美术自然眨眼验收。
- 已直接浏览9个实际不同源PNG及真Alpha合成的17帧[黑底眼部/Codex图](source-face-codex-eyes-black-review.jpg)、[淡紫全身图](source-full-lilac-review.jpg)，眼睑阶段可辨，双角与两枚交织挂饰继续存在。静态图无法证明过渡无伪影或眼睑闭合节奏自然。眼睛固定ROI相对000的premultiplied RGB平均绝对差为 [0,8.962,11.698,14.966,14.869,17.709,18.561,20.309,21.903,20.309,18.561,17.709,14.869,14.966,11.698,8.962,0]；数字不构成质量门。
- 源图复制到生产分支0张，独立新绘0张，确认需要返修的失败帧**尚无**，而非已合格。解剖接触2px、同姿态身体比例1%、家族idle→blink→idle、高清重绘母版和local runtime均not_checked。
- [Draft PR #2](https://github.com/carInHITSZ/codex-deskpet-assets/pull/2)保持WIP；当前状态 `candidate_source_technical_checked_visual_pending`，不得填 `web_sequence_checked`。
