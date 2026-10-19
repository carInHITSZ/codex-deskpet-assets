# idle r01 检查点（CI实测后）

- PR：https://github.com/carInHITSZ/codex-deskpet-assets/pull/1；分支：`web/idle-r01`。
- 当前实物：20张1024² RGBA候选帧，20张1254² RGBA原始母版；保留原文件和Git blob来源，未重画/替换。
- 技术：GitHub Actions [#39231855426](https://github.com/carInHITSZ/codex-deskpet-assets/actions/runs/39231855426) 实际解码20帧，结果success/20通过/0失败，Alpha min=0 max=255，最小边距128，bbox bottom=896。逐帧数据：`qa/pixel-audit.json`。
- 美术：仅5张关键静帧被观看；其他15张未核实；三档三轮实播/循环及家族衔接均`not_checked`。
- 合格绘制新帧：0。不得视为已web_sequence_checked、local_accepted或runtime_ready。
- 阻断：Only 5 keyposes visually viewed; visual QA still pending for intermediate frames；No 100%/50%/25% three-cycle actual visual playback in current session；No anatomical contact ≤2px or 1% keypoint-scale measurement；No idle loop seam/family transitions completed；New redraw attempt had identity drift and was rejected。
- 下一步：Visually review all 20 candidate frames on black/white/lilac backdrops and compare against the master, particularly Codex knot/horn/wing/root/head scale. Fix any failed frames with reference-locked redraw, then actually play three complete cycles at 100%,50%,25% and verify seam/contact; keep this Draft PR unmerged until then.
