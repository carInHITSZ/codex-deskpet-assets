# idle r01 – 恢复检查点

- 分支：`web/idle-r01`；基线main：`eba7dd6478744b1e3820963b024c0302e2d05da8`。
- 本次候选暂存：`0, 4, 8, 12, 16`；尚待暂存：`1, 2, 3, 5, 6, 7, 9, 10, 11, 13, 14, 15, 17, 18, 19`。
- 已确认来源缺帧：无。**已验收成品帧：0；整个动作未验收**。
- 真实Git blob复制，未重绘；原母版另存不可覆盖旧源图。
- 技术检查：仅以源元数据和关键姿态可视检查为限；Alpha完整测量与多速实播均未检查。
- 阻塞：需全帧美术/Alpha QA、三档三轮实播、loop接口；本地接入验收另行完成。
- 下一步：Stage the remaining 15 selected existing idle candidate PNGs and corresponding original masters with their exact source Git blob SHAs; run byte/header/alpha/margin validation, inspect all frames at three actual playback speeds, repair any verified defects before marking web_sequence_checked.
