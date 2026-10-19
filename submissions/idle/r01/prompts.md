# idle r01 – 已使用的来源与制作约束

## 已暂存的真实素材

- 000: `groups/idle/images/initial/master_front.png`（标准帧）和 `assets/masters/masters/master_front.png`（原始母版），完整字节原样复用；Git blob `7e8b5e5a3f15bd83a5c5dd5da476dff0e073e611`.
- 004: `groups/idle/images/poses/idle_inhale_start.png`（标准帧）和 `assets/masters/generation-only/poses/idle_inhale_start.png`（原始母版），完整字节原样复用；Git blob `e86326bc208bff2e92942a4220bfd9e43604e2f8`.
- 008: `groups/idle/images/poses/idle_inhale_mid.png`（标准帧）和 `assets/masters/generation-only/poses/idle_inhale_mid.png`（原始母版），完整字节原样复用；Git blob `7ad6740c315b342aa7295c47841c66da572378fa`.
- 012: `groups/idle/images/initial/idle_breath_peak.png`（标准帧）和 `assets/masters/masters/idle_breath_peak.png`（原始母版），完整字节原样复用；Git blob `5f57e3b726edc1bae97f6b64536acc45aa9f3dba`.
- 016: `groups/idle/images/poses/idle_exhale_mid.png`（标准帧）和 `assets/masters/generation-only/poses/idle_exhale_mid.png`（原始母版），完整字节原样复用；Git blob `303c52149a703f1cd10ca3a9d4532f66a7ee15ab`.

## 约束

执行 main/CONTINUE.md、STANDARD.md V3、CORRECTIONS.md、groups/idle/PROMPT.md 与 planned-frames.jsonl。角色必须保留白发紫瞳、两角两翼一尾、白紫服饰、Codex连续交织饰物（不可变花）。动画目标微弱呼吸，脚底接触锁定；12fps、20帧、循环；站姿名义锚点[512,896]，所有技术与视觉验收必须实测。新增生成样例不符合身份已拒收。
