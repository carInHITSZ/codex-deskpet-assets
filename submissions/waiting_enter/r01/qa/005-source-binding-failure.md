# waiting_enter/005 — 参考绑定实测失败，拒收未上传（2026-10-19T12:32:56.072Z）

- **Reference-binding test result**: 005 output rejected (wrong person appearance: eye color/clothing/head ornament; excessive lean). No new drawing candidate or source master was uploaded.
- Actual generator invocation produced native 1254×1254 RGBA, 1,082,475 bytes, SHA256 13e8dc257d5fd439985d448b02f0233e725d4421157a554eb04ed6c338796288; gen ID b3d0712c-c96e-43db-a5d5-dd5c22ac1026. It was only a local *rejected attempt*, not an accepted retained master.
- GitHub tools can read and display original images, but actual image generator did not accurately bind those returned image references as edit inputs. Do not infer reference fidelity from visible connector images.
- Minimum next-turn PNG upload set: main/reference/master_front_1024.png; branch/submissions/waiting_enter/r01/candidates/waiting_enter_004_ref_repaint_candidate.png; branch/submissions/waiting_enter/r01/candidates/waiting_enter_008_ref_repaint_candidate.png; main/groups/waiting_enter/images/frames/waiting_enter_frame_005_v2.png.
- Once files are user-attached, retry frame005 with source-locked editing, validate before advancing 006/007. All 3-speed playback/family/runtime checks still not_checked.

### 计数边界

- 本次调用确实返回一张新图，但角色身份和姿态明显错误，判为 `rejected_not_candidate`；**0张本轮新增可交付候选，0张新增上传母版，0帧远端新提交**。
- 原始004、008候选、母版和历史证据保留原样；仍各1候选+1母版、正式验收0。
- 如需查证错误图，本次本地路径与SHA已记录于CHECKPOINT JSON，未向GitHub推送不合格二进制。

### 尚未解决的独立风险

005旧源先前包围盒高度676px且不与两端轻微前倾尺度自然衔接；008微前倾和双足解剖接触尚未量化，均不允许直接宣称通过。
