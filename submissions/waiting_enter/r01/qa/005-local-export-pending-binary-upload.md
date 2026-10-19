# waiting_enter/005 — local new image export, binary upload pending

Date: 2026-10-19. This is a **LOCAL CANDIDATE RECORD, NOT A REMOTE IMAGE SUBMISSION**.

## Actual locally retained files

- `candidates/waiting_enter_005_ref_repaint_candidate.png` — 1024 × 1024, PNG RGBA8, 448,589 bytes, SHA-256 `c7c7f161a913d2be927c410f7e1d1056bbb6094b5f6ea20f5e30216412e7ed15`; **not present on this GitHub branch** at time of report.
- `masters/waiting_enter_005_gen_77070941_original.png` — native 1254 × 1254 PNG RGBA8 unmodified generator result, 1,219,336 bytes, SHA-256 `8fd37c9ce0ad5d7cb5d0151d7acfd557ea1dd8d695c33ef80dfb9fe4a09cbb86`; **not present on this GitHub branch** at time of report.
- Local staged ZIP: `waiting_enter_005_staged_for_github.zip`, SHA-256 `962017d9e0cce39bb9975002d1402ee6c5c56b088e877b28d6dd9775552c191d`. This is a local conversation download, *not hosted in the repository*.
- Generation: OpenAI image_gen, recorded ID `77070941-0929-4d10-8aef-a9458c6f610b`; generated in earlier assistant turn using four user-attached source PNGs. Underlying reference conditioning cannot be independently validated just from visible output; manual identity review remains pending.

## Export and QA actually performed

Uniform export scale `0.5964585274930102`, resized new 1254-square generated master to 748×748 with premultiplied-alpha-aware area resampling and straight-alpha output, then translated by [131,204] onto transparent 1024-square canvas. Anchor [512,896], duration 50 ms. PNG export has alpha>8 bbox [300,255,758,896], approximately 641px high, zero alpha at canvas borders, no detached alpha>8 components. Background-composited black, white and lilac partial comparisons were generated for local visual review. 004 and 008 are still **unaccepted** endpoints.

Two discrete sole regions are visible near y=891..896, but **anatomical contact error <=2px was not established**; torso-lean angle and proportional landmark agreement were **not measured**. Exact interwoven Codex topology, full 003→009 consecutive progression, all 17 frames at 100%/50%/25% three rounds each, waiting_loop transitions and runtime remain **not_checked**.

## Blocker / next action

GitHub's connected write API can create text and git blobs from supplied strings but cannot directly import a local container binary; the local shell has no resolving network route to `github.com`. Therefore **no 005 PNG upload and no SHA-256 remote readback** have taken place.

Transfer the two local PNGs to their named paths on this existing production branch (without touching `main`), then fetch and verify the exact remote bytes, upload the staged manifest/QA/prompt and update CHECKPOINT+Draft PR #3. Only after a successful image upload should 006/007 generation and continuous sequence checks resume.

Remote newly submitted 005 images: **0**. Newly art-accepted 005 frames: **0**.
