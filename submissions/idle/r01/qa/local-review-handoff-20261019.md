# idle r01 — 本地美术与集成交接（2026-10-19）

## 结论（非美术验收）

网页本轮在现有证据下未确认任何必须返修的帧，且没有独立完成可观察连续动画的人工式美术判断。因此正式标记为 `pending_local_review`，不升格 `web_sequence_checked`；不修改任何旧PNG/母版、不重复技术CI或三速机械测试，网页端暂时跳过 idle，等待本地给出**具体失败帧与证据**再定向返修。

- 既有候选：20/20帧，20份原母版，已原样暂存；原有真实PNG复制20张，**本次新增复制0张**；合格独立新绘0张，确认需要返修0张（不代表整组艺术通过）。
- 历史有效证据：PNG/RGBA技术CI [#39231855426](https://github.com/carInHITSZ/codex-deskpet-assets/actions/runs/39231855426)，机械Chrome 100%/50%/25%各三轮 [#39232840986](https://github.com/carInHITSZ/codex-deskpet-assets/actions/runs/39232840986)；真实Alpha合成/ROI代理 [#39237080876](https://github.com/carInHITSZ/codex-deskpet-assets/actions/runs/39237080876)，20帧面部/Codex静态裁切 [#39237945143](https://github.com/carInHITSZ/codex-deskpet-assets/actions/runs/39237945143)。**这些是已有成果，此交接不重复计功。**
- Alpha事实：y≥896的像素Alpha最大2/255，黑底合成最大通道1/255；不能把查看器疑似亮点直接判为可见污染。
- 足底ROI代理横向幅度约2.23/2.02px非解剖点接触；019→000像素MAE 9.4961非循环观感门槛。

## local review 待执行清单（全部未验收）

1. 在1024×1024 RGBA的20个真实文件上独立标注各自解剖左/右脚、鞋底支持相位与接地点；逐相位验证≤2px，失配则附帧号、截图与坐标。未知接触点保留null。
2. 按统一人物身体比例标注角尖、头/肩/胯、翼根与脚底，对相同姿态比较比例偏差≤1%；报告度量定义及逐帧数值，不用alpha bbox作人体尺度代理。
3. 亲眼观察真实连续动画：100%/50%/25%，每档≥3轮，评估呼吸是否自然、头发/翼/饰品是否闪跳、身体有无异常形变；重点检查019→000循环接缝，并记录可重现的失败帧对和速度。
4. 对005、008、013、014、016、017以原生分辨率检查翼缘、头发、服装接缝及疑似微量残色；结合黑/白/淡紫真实合成判断是否可见。逐帧核对Codex连续交织拓扑（非花朵），只有实证失败才返修。
5. 当blink/waiting相关动画及idle均完成美术确认后，测试idle↔blink、idle→waiting_enter→waiting_loop→waiting_exit→idle的进出场与接触连贯性；未验收的依赖不等于已失败。
6. 本地桌宠内验DPI 100/125/150%、多屏、拖动、隐藏恢复、内存与事件中断；网页端不能签发local_accepted或runtime_ready。

## 恢复/计数

状态：`pending_local_review`；`webChecks=not_accepted`；`localAcceptance=false`；`runtimeAcceptance=false`。新图片0；修图0；本轮原样复制0；新的机械测试0；新增**交接结论与本地待检清单**1。收到带证据的指定失败帧后回到web/idle-r01同一Draft PR，不创建重复PR。
