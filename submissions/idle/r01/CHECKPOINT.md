# idle r01 可恢复检查点

- 分支：`web/idle-r01`；Draft PR：https://github.com/carInHITSZ/codex-deskpet-assets/pull/1
- 当前实际暂存：20张候选标准PNG和20张原始母版，来自main已有素材的原样Git blob引用。
- 真实新增且正式验收的高清独立绘制帧：**0**；当前来源缺帧：0。
- 已检：20张候选PNG的文件头（全部1024x1024 RGBA8非交错）；可视检查静态关键帧5/20，未通过正式验收。
- 未检：像素级真Alpha与边距、所有帧美术身份、三档三轮真实播放、循环缝和家族衔接、本地运行。
- 本分支只能按clip合并进度，不能覆盖其他生产PR的状态。
- 下一条具体操作：Run pixel-level PNG alpha/margin/halo QA for idle 000–019; visually inspect all frames against reference; repair rejected poses with locked character identity; actually play each of 100%,50%,25% for 3 full loops, inspect seam/contact and family exits; document measured outcomes before state advance.
