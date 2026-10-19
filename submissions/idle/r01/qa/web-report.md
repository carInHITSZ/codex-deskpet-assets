# idle r01 — 真实技术检查与待做美术验收

更新时间 UTC：2026-10-19T09:43:52.084Z

## 已经完成

- 实际暂存 main 已有20张候选PNG和20张原始母版；所有文件为字节级原样复制，**本次合格新绘0张**。
- 通过GitHub Actions [运行#39231855426](https://github.com/carInHITSZ/codex-deskpet-assets/actions/runs/39231855426) 在Ubuntu/Python/Pillow上**实际打开并解码全部20张独立PNG与原始母版**，任务返回success。详见 `qa/pixel-audit.json`。
- **20/20技术通过、0失败**：每张PNG为1024×1024 RGBA、Alpha最小0最大255，兼有透明/半透明/不透明像素，alpha>8区域与边缘至少128像素，20张bbox下边界均为y=896，原始母版实际尺寸全部1254×1254、模式RGBA；相邻帧没有完全相同的像素帧。
- 静态视觉仅实际查看000、004、008、012、016；可确认身份主要元素基本存在但不构成全部逐帧美术验收。
- 另生成过一张1254×1254样图（SHA256 `7e1b0c1692d7698290f04fb6f45fcb73681f896246e34b85dfea1ab797e4c272`），身份/服饰/翼幅偏离主基准，拒收且未进生产帧。

## 检查矩阵

| 项目 | 结果 | 证据 |
|---|---|---|
| GitHub二进制写入及远端再次读取 | checked | 已存在PR及各帧Git blobs |
| 标准PNG RGBA8、透明像素、Alpha bbox、安全边距、原母版尺寸 | checked_pass (20/20) | GitHub Actions #39231855426 |
| 逐帧20张角色身份/挂饰/四肢的视觉检查 | partial (5/20) | 只看过五张静态帧 |
| 黑白紫三背景下异常色边 | not_checked | 需要背景切换人工查看 |
| 同姿态关键点比例误差≤1% | not_checked | 尚无人体解剖关键点测量 |
| 足底接触漂移≤2px | not_checked | 全帧bbox y=896不是双足支撑点证据 |
| 100%三轮实际播放 | not_checked | 没有执行本次真正的视觉播放 |
| 50%三轮实际播放 | not_checked | 同上 |
| 25%三轮实际播放 | not_checked | 同上 |
| 循环/家族进出场串联 | not_checked | 不能单凭独立静帧判断 |
| 本地DPI/多屏/完整桌宠 | not_checked | 非本次执行范围 |

技术检查的主体边距最小值为 **128 px**，但该指标只测框定Alpha边缘；不能作为角色动作质量合格的依据。

## 当前状态与下一步

`technical_checked_visual_pending`（20个候选来源已封装，20/20像素技术预检通过，0个新绘成品被验收）。**没有达到web_sequence_checked。**

Visually review all 20 candidate frames on black/white/lilac backdrops and compare against the master, particularly Codex knot/horn/wing/root/head scale. Fix any failed frames with reference-locked redraw, then actually play three complete cycles at 100%,50%,25% and verify seam/contact; keep this Draft PR unmerged until then.
