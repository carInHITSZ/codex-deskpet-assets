# idle r01 续作检查点（机械播放已实测）

- 分支：`web/idle-r01`；Draft PR：https://github.com/carInHITSZ/codex-deskpet-assets/pull/1。
- 候选来源：20张现有标准RGBA PNG +20份1254x1254原始母版，均按Git blob原样引用；新绘正式验收0。
- 像素检查：[Actions #39231855426](https://github.com/carInHITSZ/codex-deskpet-assets/actions/runs/39231855426) 20/20通过，最小Alpha主体边距128px，bbox下界896。
- 真实网页测试：[Actions #39232840986](https://github.com/carInHITSZ/codex-deskpet-assets/actions/runs/39232840986) 100%/50%/25%各三轮；每档20图解码成功、60次Canvas绘制正确、序列顺序正确、0页面异常；**只算机械通过，不算视觉验收**。
- 实际查看20张独立PNG静帧、帧019黑白淡紫截图；按标准逐项身份、细节/色边、loop与连接仍待确认。
- 本地多屏/DPI/桌宠未检；其他53动作组和家族衔接未完成。
- 当前状态：`mechanical_playback_pass_visual_review_pending`，**禁止升级web_sequence_checked**。
- 下一步：Inspect all 20 frames in real black/white/lilac compositing with focus on suspected edge speckles, measure foot contacts and global keypoint scale, check browser motion visually at three speeds and loop seam, repair reference-locked failed poses; then validate adjacent idle/blink/waiting transitions. Do NOT claim web_sequence_checked without those gates.

## 2026-10-19T10:26:18.550Z — 新增实测取证

- 新增读取全部20张原生PNG并审阅经真实Alpha合成的黑/白/淡紫20帧缩小审阅图；此为静态复核，不是原生分辨率全要素美术验收。
- 取证 Actions [#39237080876](https://github.com/carInHITSZ/codex-deskpet-assets/actions/runs/39237080876)；[forensics.json](qa/diagnostic/forensics.json) 和5张缩小/脚部QA可见图已上传，源图没改。
- 脚下疑似品红噪点：实际最大Alpha≤2，黑底合成最大通道≤1；暂不删图。优先原生分辨率复核帧005、008、013、014、016、017，**尚无确认需替换的帧**。
- 双鞋轮廓ROI X范围左2.23px、右2.02px（Y各1px）仅为代理，接触点正式验收not_checked；首尾像素差9.4961/相邻中位数1.092，仅是诊断。
- 本会话没有可靠连续视觉观察、没有合格新绘、没有进行家族拼接；保持现有状态与原20图。下一步详见CHECKPOINT.json的nextExactAction。
