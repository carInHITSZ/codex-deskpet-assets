# idle r01 — 真实技术检查与待做美术验收

更新时间 UTC：2026-10-19T09:43:52.084Z

## 已经完成

- 实际暂存 main 已有20张候选PNG和20张原始母版；所有文件为字节级原样复制，**本次合格新绘0张**。
- 通过GitHub Actions [运行#39231855426](https://github.com/carInHITSZ/codex-deskpet-assets/actions/runs/39231855426) 在Ubuntu/Python/Pillow上**实际打开并解码全部20张独立PNG与原始母版**，任务返回success。详见 `qa/pixel-audit.json`。
- **20/20技术通过、0失败**：每张PNG为1024×1024 RGBA、Alpha最小0最大255，兼有透明/半透明/不透明像素，alpha>8区域与边缘至少128像素，20张bbox下边界均为y=896，原始母版实际尺寸全部1254×1254、模式RGBA；相邻帧没有完全相同的像素帧。
- 现已逐张实际查看全部20张独立静态PNG（默认黑底PNG渲染）；之前记录的五个关键帧也在其中。静态全帧观看不等于按规范逐项通过；可确认身份主要元素基本存在但不构成全部逐帧美术验收。
- 另生成过一张1254×1254样图（SHA256 `7e1b0c1692d7698290f04fb6f45fcb73681f896246e34b85dfea1ab797e4c272`），身份/服饰/翼幅偏离主基准，拒收且未进生产帧。

## 检查矩阵

| 项目 | 结果 | 证据 |
|---|---|---|
| GitHub二进制写入及远端再次读取 | checked | 已存在PR及各帧Git blobs |
| 标准PNG RGBA8、透明像素、Alpha bbox、安全边距、原母版尺寸 | checked_pass (20/20) | GitHub Actions #39231855426 |
| 逐帧20张静态身份检查 | static_viewed_20_of_20_pending_art_acceptance | 本次再次逐张看20张原生PNG，正式身份验收仍未完成 |
| 黑白紫三背景合成 | preliminary_static_review_only | 本次真实Alpha合成20×3并审阅缩小版，原生尺寸逐帧边缘仍未正式验收 |
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

## 本次新增：真实浏览器三档三轮机械播放

使用GitHub Actions [运行 #39232840986](https://github.com/carInHITSZ/codex-deskpet-assets/actions/runs/39232840986) 中的真实Google Chrome headless + Puppeteer，加载`qa/preview.html`本地HTTP页面，预解码20张PNG，并在HTML Canvas逐帧展示；按真实时钟依次执行100%、50%、25%各3轮。三档均成功；完整逐项记录在 `qa/browser-playback-current.json`。

100%：三轮60次真实Canvas绘制，实际5000ms，最大计划误差0.57ms，页面异常0
50%：三轮60次真实Canvas绘制，实际10000ms，最大计划误差0.80ms，页面异常0
25%：三轮60次真实Canvas绘制，实际19999ms，最大计划误差0.63ms，页面异常0

浏览器实际截图共9张（各速度终点帧019在黑/白/淡紫背景），已保存到该 Actions run 的 `idle-r01-browser-playback` artifact；该实验记录是本次新执行，而非引用以前的 `qa/browser-playback-records.json`。

**范围限制：**自动化只测解码、实际Canvas更新、60个帧序列和壁钟节奏。脚本标记 `visuallyAccepted:false`；它无法替代人眼逐帧/动画的身份、呼吸细腻度、足底解剖接触、循环首尾观感或家族衔接。接触误差与连续动作仍未被正式美术验收。

黑/白/淡紫截图（帧019）的实际合成已人工打开检查，未见明显成片色块外溢；此前原图查看器显示的零星亮点是否仅为极低Alpha像素仍需对其他帧逐个验证，不能宣布全帧无色边。

**状态仍为 mechanical_playback_pass_visual_review_pending，正式验收通过帧数0。**

## 2026-10-19 续作：实际取证与多背景合成（新增，未修图）

源图为已有 `frames/idle/000.png` 至 `019.png`，未改任何帧或母版。新程序 `scripts/idle_r01_forensics.py` 在 GitHub Actions [#39237080876](https://github.com/carInHITSZ/codex-deskpet-assets/actions/runs/39237080876) 中实际用 Pillow+NumPy 读取20张原生1024² RGBA帧，合成黑/白/淡紫三种背景；输出逐帧[数值报告](diagnostic/forensics.json)、三份完整画面[黑](diagnostic/overview-black-review.jpg)/[白](diagnostic/overview-white-review.jpg)/[淡紫](diagnostic/overview-lilac-review.jpg)审阅图、两份局部脚部[000–009](diagnostic/feet-000-009.png)/[010–019](diagnostic/feet-010-019.png)；高分辨率PNG审阅底稿亦保留。

本次通过GitHub授权读取20/20真实PNG并查看原始黑底静帧，也已打开以上实际合成联系图（联系图为了可审阅经过缩小/有损JPEG输出，仅作为QA，不充作生产帧）。从原始PNG查看器观察：005、008、013–014、016–017等帧边缘/脚下存在疑似粉紫碎点。**实际Alpha量化纠正了脚下“明显污染”的初判**：全部20帧的y>=896区域最大Alpha仅为2/255，黑底合成单通道最高亮度仅1/255，未证实属于正常Alpha渲染下可见的严重污染。因此不清理这些区域，避免破坏合格原稿。完整高分辨率边缘仍待审查，不将0个>7px远离主体的高饱和信号误推为全部边缘完美。

鞋底ROI亮度/Alpha代理测量：画面左侧鞋横向波动范围2.23px、纵向1px；右侧横向2.02px、纵向1px。**这不是独立标注的脚部解剖接触点，不能通过标准≤2px gate；所有anatomical/contactPoints保持null。** `019→000` 固定视窗premultiplied RGB平均绝对差9.4961，约为普通相邻帧中位数1.092倍；只能量化差异，不能宣称视觉循环接缝平顺/呼吸节奏通过。

- 本次确认需更换的失败PNG：**尚无**（未确认，不能编造失败号）；原生分辨率优先复核 `005,008,013,014,016,017`。无依据的清理/重画未执行。
- 原20张候选及母版保持原样；新增被美术验收的重绘图 **0**。
- 已有100%/50%/25%各三轮自动播放仅是旧机械成功证据。本次没有重跑未变化的素材进行“伪进度”，也没有可作为美术接受的真人持续播放观察；`visualLoop`、`anatomicalContacts`、`familyTransition`、`runtime`均未验收。
- 下一项：在完整1024分辨率逐项比对挂饰拓扑、脸/服饰/翼与关键帧，标出真实双足解剖点并复测；将20帧以真实连续动画观看3速x3后评价首尾/呼吸。仅对确认失败帧进行身份锁定重绘，引用主基准及相邻**已验收**关键帧。

状态仍为 `mechanical_playback_pass_visual_review_pending`，不是 `web_sequence_checked`；`local_accepted/runtime_ready` 均 false。
