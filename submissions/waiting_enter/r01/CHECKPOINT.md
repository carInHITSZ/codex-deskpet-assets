# waiting_enter / r01 checkpoint (2026-10-19T12:27:42.911Z)

- 最新核对HEAD（文档提交前）：`907393386dad335fe07dbcaf01b00f4235ebc8b1`；Draft PR #3，分支`web/waiting-enter-r01`，未合并main。
- 分支真实新绘候选 **004、008共2帧**，对应**2张未修改的原始生成母版**，合计4个PNG文件；非4帧；本次记录纠错不新增生图。
- 新绘候选验收通过 **0帧**。旧候选源17/17存在不等于正式验收通过；无006/007新绘远端证据。
- 004历史记录见`manifest-004-generated.json`；008补登记`manifest-008-generated.json`、`prompts-008.md`、`qa/008-generated-candidate-review.md`。
- 静态源图已读主基准、003、004、005、006、007、008及009。005旧源相对004有尺度风险。008头部接近正向，但姿态角、真实双足接触、Codex精确拓扑及全片顺序仍需复核。
- 完整`003→004→005→006→007→008→009`动态检查、100/50/25%×3、waiting_loop衔接、local/runtime：`not_checked`。
- 下一步：实际确认生成器可使用**原始PNG参考像素**，优先复核004/008关键姿态，确定005返修，再重绘006/007；每张新图单独提交回读。

## 本轮参考锁定生成实验

- **Reference-binding test result**: 005 output rejected (wrong person appearance: eye color/clothing/head ornament; excessive lean). No new drawing candidate or source master was uploaded.
- Actual generator invocation produced native 1254×1254 RGBA, 1,082,475 bytes, SHA256 13e8dc257d5fd439985d448b02f0233e725d4421157a554eb04ed6c338796288; gen ID b3d0712c-c96e-43db-a5d5-dd5c22ac1026. It was only a local *rejected attempt*, not an accepted retained master.
- GitHub tools can read and display original images, but actual image generator did not accurately bind those returned image references as edit inputs. Do not infer reference fidelity from visible connector images.
- Minimum next-turn PNG upload set: main/reference/master_front_1024.png; branch/submissions/waiting_enter/r01/candidates/waiting_enter_004_ref_repaint_candidate.png; branch/submissions/waiting_enter/r01/candidates/waiting_enter_008_ref_repaint_candidate.png; main/groups/waiting_enter/images/frames/waiting_enter_frame_005_v2.png.
- Once files are user-attached, retry frame005 with source-locked editing, validate before advancing 006/007. All 3-speed playback/family/runtime checks still not_checked.
