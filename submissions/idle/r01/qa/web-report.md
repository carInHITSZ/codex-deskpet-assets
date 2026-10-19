# idle r01 网页端生产检查报告

更新时间 UTC：2026-10-19T09:36:10.568Z

## 实际成果

- 已远端暂存20/20张现有候选PNG、20/20份对应原始母版；均为Git blob字节级原样引用，没有把复制文件记成新绘。
- 实际通过GitHub读取全部20张PNG的base64并解析文件IHDR：20/20拥有PNG签名、1024×1024、8bit RGBA(color type 6)、non-interlaced。**仅验证文件头，尚未逐像素解码Alpha/边界**。
- 本次实际查看静态关键帧000、004、008、012、016，对基本白紫身份、双翼两角尾巴和交织饰物进行了部分观察；其余15帧未独立视觉复核。
- 单独使用生成工具得到1254×1254 RGBA新尝试，SHA256 `7e1b0c1692d7698290f04fb6f45fcb73681f896246e34b85dfea1ab797e4c272`，因脸型/头身、服饰和翼展偏离主基准，**拒收并未添加到提交**。
- qa/browser-playback-records.json是仓库旧记录（其中idle visualAccepted=false），不是本会话实际完成的三速美术检查。

| 检查 | 结果 |
|---|---|
| 已授权GitHub访问/创建二进制blob/远端提交 | checked |
| 20张候选PNG签名、尺寸、RGBA8、非交错 | checked |
| 像素级Alpha范围/占比/实际边距与色边 | not_checked |
| 全20张角色身份/挂饰/肢体 | partial (only 000,004,008,012,016 viewed) |
| 真实双脚接触偏差≤2px与骨架比例≤1% | not_checked |
| 100%播放3轮并观察 | not_checked |
| 50%播放3轮并观察 | not_checked |
| 25%播放3轮并观察 | not_checked |
| 循环缝/进入退出/家族衔接 | not_checked |
| 本地桌宠运行/DPI多屏 | not_checked |

**当前状态：candidate_uploaded_needs_validation；完成验收帧数0。** 不满足web_sequence_checked门槛，不得视为local_accepted/runtime_ready。

下一步：Run pixel-level PNG alpha/margin/halo QA for idle 000–019; visually inspect all frames against reference; repair rejected poses with locked character identity; actually play each of 100%,50%,25% for 3 full loops, inspect seam/contact and family exits; document measured outcomes before state advance.
