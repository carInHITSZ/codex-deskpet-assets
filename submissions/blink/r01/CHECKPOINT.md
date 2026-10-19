# blink r01 真实候选源技术预检恢复点

17个帧位引用main原始候选，其中正反程显式复用9种来源。暂无新增或已验收重绘，未复制现有PNG。技术与真实浏览器三速测试进行中；所有视觉美术验收和idle接口依赖为not_checked。

## 2026-10-19T10:43:43.151Z — 本次真实源图/浏览器检查结果

- [Actions #39239051047](https://github.com/carInHITSZ/codex-deskpet-assets/actions/runs/39239051047)实际解码**17/17 RGBA8、1024²**并确认Alpha/margin技术检查通过，9个独立来源，按计划正反对称。
- 原始源图从未复制至生产分支，也未重绘/接受新图：**0张**。
- Chromium实际按100%、50%、25%速度各播放3次，准确绘制51次/档，全部机械pass。机器人实际连续观看与美术通过**not_checked**。
- [source-audit.json](qa/source-audit.json) [browser-playback.json](qa/browser-playback.json)，[眼部/双角/挂饰黑底对照](qa/source-face-codex-eyes-black-review.jpg) [淡紫全身](qa/source-full-lilac-review.jpg)已实际查看。眼睛逐渐闭合并重新张开；视觉节奏仍待验收。
- 头尾源图SHA256相同，但与idle循环最后一张的拼接**not_checked**；足部精确接触、人体比例、本地运行亦not_checked。
- [Draft PR #2](https://github.com/carInHITSZ/codex-deskpet-assets/pull/2)保持未合并。
