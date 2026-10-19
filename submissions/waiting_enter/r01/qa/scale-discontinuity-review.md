# waiting_enter/r01 — 已有关键姿态视觉与尺度跳变复核

## 取证范围（2026-10-19）

通过已授权 GitHub 连接器实际读取并在本会话原图尺寸视图中打开以下真实1024×1024 PNG：

- `reference/master_front_1024.png`、`groups/waiting_enter/images/poses/waiting_attention_forward.png`（时间线帧004）
- `groups/waiting_enter/images/poses/waiting_lean_forward.png`（008）
- `groups/waiting_enter/images/poses/waiting_tilt_begin_v3.png`（012）
- `groups/waiting_enter/images/poses/waiting_expectant_base.png`（016）

按main的`groups/waiting_enter/current-timeline.json`逐一核实槽位，并从真实资产登记`assets/catalog.json`读取源图的Alpha>8包围盒记录。以下只是静态测量和观看结论，不伪称已观察连续动画；所列bbox均来自main资产索引，非新跑的像素CI。

| 槽位 | 资产 ID | bbox Alpha>8 [left,top,right,bottom] | 轮廓高度px | 与000的差别 |
|---|---|---|---:|---:|
| 000 | master_front | [293,256,753,896] | 640 | 0% |
| 004 | waiting_attention_forward | [333,373,717,897] | 524 | -18.13% |
| 008 | waiting_lean_forward | [321,347,728,897] | 550 | -14.06% |
| 012 | waiting_tilt_begin_v3 | [278,221,777,898] | 677 | +5.78% |
| 016 | waiting_expectant_base | [282,223,771,898] | 675 | +5.47% |

另：004→008轮廓高度+26px，008→012 +127px (+23.09% relative to 008)；000→004 -116px。这里的高度变化是带尾巴/角/衣服的**整体轮廓代理**，不等于经标注的人体关键点比例误差，但与帧004/008明显较小、012/016恢复放大的实际视觉观察一致。四张关键姿态底边y=897/897/898/898，说明该异常不是简单的整体向下移动。计划明确前倾上限4°、双脚固定，因此应视为关键姿态之间的严重尺度/构图连续性风险，不能据此声明任何一帧合格。

已有 `qa/waiting-family-qa-review.json` 记录本组最大估计脚部移动32.918px、头部外轮廓宽度变化比例0.37972且`geometryProxyMetricsPassed=false`。该已有QA是**轮廓代理**而非解剖2px/头身比例1%检验，故本次没有把它标成严格阈值的正式失效。新增加的是指定**004、008相对000/012/016的真实对应帧与静态观察**，可供定向返修。

## 处理决策

- **确认问题类别：**`scale_and_framing_discontinuity_observed`；重点返修/复核位置`004,008`，再沿`000→004→008→012→016`逐段复核中间帧；这是帧间异常定位，不是判定其它12帧一定通过。
- 当前缺少支持主基准+相邻帧的可靠身份锁定高清重绘链。本会话对独立缺帧walk_left/001试生图，工具实际输出错误的GitHub网页截图，已拒收，不上传也不计新增；因此**没有**根据上述发现盲目放大原有PNG或进行不合规修图。
- V3统一1024² RGBA、固定角尖/鞋底比例、Codex交织挂饰非花、双角双翼尾结构；不得采用逐帧bbox回正、低清放大、复制或透明混合掩盖根因。
- 没有新生成的waiting_enter图、没有重跑旧机械播放、没有伪造三速循环观感或本地集成成功。17槽均有旧候选，不代表完整序列视觉验收。

## 待动作（状态保持未验收）

1. 具备真正参考图输入+文件导出的角色锁定重绘能力后，先为`004`、`008`制作接近640px身体基准的新母版，分别对照角色主基准、帧000、012，不使用插值放大。
2. 每个重新生成的独立文件分别验证真实RGBA、原始母版尺寸、1:1面部/Codex拓扑、左右翼尾和衣服/鞋子完整性；只有通过才代入候选序列。其余中间帧视结果定向返修，不承诺旧源可无条件复用。
3. 有合格关键姿态后再核真实人体同姿态≤1%比例、双足解剖接触≤2px，真实连续100/50/25%各3轮，衔接waiting_loop/exit须等依赖合格。
4. 本地桌宠/DPI多屏/运行时集成独立为`not_checked`。

## 本次实际计数

新生成/返修合格PNG：**0/0**；本轮原样复用并复制到新分支PNG：**0**；新增验证结论：**1项静态分段尺度异常定位**，此前的waiting family QA无重复执行。状态：`needs_revision_reference_generation_blocked`，`web_sequence_checked=false`，Draft PR，不合并main。
