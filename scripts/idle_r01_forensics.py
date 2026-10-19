#!/usr/bin/env python3
"""Evidence-only idle PNG forensics. Does not modify production frames or grant art acceptance."""
from __future__ import annotations
import argparse
import json
import os
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

PALETTES = {"black": (0, 0, 0), "white": (255, 255, 255), "lilac": (226, 213, 244)}
FRAME_COUNT = 20
SHOE_ROIS = {
    "image_left": (473, 852, 512, 903),
    "image_right": (512, 852, 556, 903),
}


def alpha_compose(image: Image.Image, bg: tuple[int, int, int]) -> Image.Image:
    background = Image.new("RGBA", image.size, bg + (255,))
    return Image.alpha_composite(background, image).convert("RGB")


def foot_proxy(alpha: np.ndarray, roi: tuple[int, int, int, int]) -> dict:
    """Image-plane opaque-lowest-pixel proxy, NOT measured anatomical plantar landmark."""
    left, top, right, bottom = roi
    patch = alpha[top:bottom, left:right]
    ys, xs = np.nonzero(patch >= 128)
    if len(ys) == 0:
        return {"x": None, "y": None, "kind": "not_measured", "reason": "no_alpha_ge_128"}
    y_bottom = int(top + ys.max())
    contact_x = xs[(top + ys) >= y_bottom - 2] + left
    return {"x": round(float(contact_x.mean()), 2), "y": y_bottom,
            "pixelSupport": int(len(contact_x)),
            "kind": "opaque_bottom_proxy_not_anatomical_contact"}


def analyze_one(im: Image.Image, index: int) -> tuple[dict, np.ndarray]:
    rgba = np.array(im, dtype=np.uint8)
    alpha = rgba[:, :, 3]
    rgb = rgba[:, :, :3].astype(np.uint16)
    premul = (rgb * alpha[:, :, None].astype(np.uint16) + 127) // 255
    brightness = premul.max(axis=2)
    body = alpha >= 32
    dilated = np.array(Image.fromarray((body * 255).astype(np.uint8), "L")
                       .filter(ImageFilter.MaxFilter(15))) > 0
    # Signal only: high-chroma RGB AND some alpha, separated >7px from core.
    chroma = rgb.max(axis=2) - rgb.min(axis=2)
    isolated = (alpha >= 2) & (~dilated) & (chroma >= 80)
    ys, xs = np.nonzero(isolated)
    specimens = []
    if len(ys):
        priority = np.argsort(alpha[ys, xs].astype(np.int32) * 256 +
                              chroma[ys, xs].astype(np.int32))[::-1][:12]
        for j in priority:
            x, y = int(xs[j]), int(ys[j])
            specimens.append({"x": x, "y": y, "alpha": int(alpha[y, x]),
                              "rgb": rgba[y, x, :3].tolist(),
                              "maxCompositedOnBlack": int(brightness[y, x])})
    below = alpha[896:, :]
    below_chroma = chroma[896:, :]
    report = {
        "frame": index,
        "rawAlphaBelowNominalBaseline": {
            "countNonzero": int(np.count_nonzero(below)),
            "countAlphaGt8": int(np.count_nonzero(below > 8)),
            "maxAlpha": int(below.max(initial=0)),
            "maxBlackCompositedChannel": int(brightness[896:].max(initial=0)),
            "countBlackChannelGe16": int(np.count_nonzero(brightness[896:] >= 16)),
            "countChromaGe80AlphaGe2": int(np.count_nonzero((below >= 2) & (below_chroma >= 80))),
        },
        "separatedChromaSignal": {
            "definition": "alpha>=2, raw RGB max-minus-min>=80, farther than 7 pixels from alpha>=32 core",
            "pixelCount": int(len(ys)),
            "examples": specimens,
        },
        "shoeBottomImageProxies": {key: foot_proxy(alpha, roi) for key, roi in SHOE_ROIS.items()},
        "headSilhouetteProxy": None,
        "formalAnatomicalContact": None,
        "formalKeypointScalePct": None,
        "visualAcceptance": "not_checked",
    }
    hy, hx = np.nonzero(body[245:475, 345:665])
    if len(hx):
        report["headSilhouetteProxy"] = {
            "bbox": [int(hx.min()+345), int(hy.min()+245),
                     int(hx.max()+346), int(hy.max()+246)],
            "scope": "region alpha>=32 bbox includes horns/hair; not a measured face landmark",
        }
    return report, premul.astype(np.uint8)


def delta(prev: np.ndarray, cur: np.ndarray, label: str) -> dict:
    # Compare same fixed viewport, not per-frame tight crops.
    patch_a = prev[230:924, 252:776].astype(np.int16)
    patch_b = cur[230:924, 252:776].astype(np.int16)
    gap = np.abs(patch_a - patch_b)
    per_px_max = np.max(gap, axis=2)
    return {"pair": label,
            "premultipliedRGBMeanAbsolute": round(float(gap.mean()), 4),
            "maxChannel": int(gap.max()),
            "fractionPixelsChannelDeltaGt16": round(float(np.mean(per_px_max > 16)), 6),
            "scope": "fixed x252:776 y230:924; alpha-premultiplied source pixels"}


def render_overviews(images: list[Image.Image], out: Path) -> list[str]:
    paths = []
    for palette_name, bg in PALETTES.items():
        tile_w, tile_h, cols = 270, 380, 5
        sheet = Image.new("RGB", (tile_w*cols, tile_h*4), (40, 40, 45))
        draw = ImageDraw.Draw(sheet)
        for i, im in enumerate(images):
            view = alpha_compose(im, bg).crop((250, 228, 780, 942))
            view.thumbnail((258, 348), Image.Resampling.LANCZOS)
            x = (i % cols)*tile_w
            y = (i // cols)*tile_h
            sheet.paste(view, (x+6+(258-view.width)//2, y+5))
            draw.text((x+9, y+354), f"{i:03d} | {palette_name} | composite", fill=(220, 220, 220))
        name = f"overview-{palette_name}.png"
        sheet.save(out/name, optimize=True)
        paths.append(name)
    return paths


def render_feet(images: list[Image.Image], out: Path) -> list[str]:
    paths = []
    for start in (0, 10):
        sheet = Image.new("RGB", (624, 1060), (44, 44, 48))
        draw = ImageDraw.Draw(sheet)
        for row, i in enumerate(range(start, start+10)):
            y = row*106
            im = images[i]
            for k, (name, bg) in enumerate(PALETTES.items()):
                tile = alpha_compose(im, bg).crop((425, 840, 625, 934))
                x = k*208+4
                sheet.paste(tile, (x, y))
                draw.text((x+3, y+94), f"{i:03d} {name} feet", fill=(220, 220, 220))
        name = f"feet-{start:03d}-{start+9:03d}.png"
        sheet.save(out/name, optimize=True)
        paths.append(name)
    return paths


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".")
    args = parser.parse_args()
    repo = Path(args.repo_root)
    clip = repo / "submissions/idle/r01"
    out = clip / "qa/diagnostic"
    out.mkdir(parents=True, exist_ok=True)
    originals = [Image.open(clip / f"frames/idle/{i:03d}.png") for i in range(FRAME_COUNT)]
    for i, im in enumerate(originals):
        if im.size != (1024, 1024) or im.mode != "RGBA":
            raise ValueError(f"frame {i} wrong size/mode {im.size}, {im.mode}")
        im.load()
    evidence, pixels = [], []
    for i, im in enumerate(originals):
        result, premul = analyze_one(im, i)
        evidence.append(result)
        pixels.append(premul)
    comparisons = [delta(pixels[i], pixels[i+1], f"{i:03d}->{i+1:03d}")
                   for i in range(19)]
    seam = delta(pixels[-1], pixels[0], "019->000_loop_seam")
    typical = float(np.median([v["premultipliedRGBMeanAbsolute"] for v in comparisons]))
    seam["ratioToMedianAdjacentDelta"] = round(seam["premultipliedRGBMeanAbsolute"]/typical, 4) if typical else None
    proxy_movements = {}
    for name in SHOE_ROIS:
        coords = [r["shoeBottomImageProxies"][name] for r in evidence]
        valid = [x for x in coords if x["x"] is not None]
        proxy_movements[name] = {
            "rangeXpx": round(max(x["x"] for x in valid)-min(x["x"] for x in valid), 2) if valid else None,
            "rangeYpx": max(x["y"] for x in valid)-min(x["y"] for x in valid) if valid else None,
            "interpretation": "segmentation ROI proxy only; not anatomical sole location",
        }
    report = {
        "type": "targeted_idle_r01_image_forensics",
        "originalFramesModified": False,
        "origin": "Actual committed 1024x1024 RGBA PNG files in production branch",
        "sourceGitCommit": os.environ.get("GITHUB_SHA"),
        "createdUtc": datetime.now(timezone.utc).isoformat(),
        "frameCount": len(originals),
        "method": "Pillow PNG decode; NumPy actual alpha and RGB; alpha composite over black/white/lilac; fixed-ROI pixel differences",
        "frames": evidence,
        "adjacentTransitions": comparisons,
        "loopSeam": seam,
        "shoeRoiProxyRanges": proxy_movements,
        "notChecked": ["anatomical_left_and_right_foot_2px",
                       "manual_face_and_Codex_knot_topology_at_100pct",
                       "same_pose_human_keypoint_scale_1pct",
                       "actual_human_observed_three_speed_loop_visual_acceptance",
                       "family_idle_blink_waiting",
                       "local_DPI_multiscreen_runtime"],
        "notAcceptance": "No pixel statistic substitutes for actual artistically accepted motion, anatomy, or family joins."
    }
    generated = render_overviews(originals, out) + render_feet(originals, out)
    report["diagnosticImages"] = generated
    (out/"forensics.json").write_text(json.dumps(report, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    summary = {
        "frames": len(originals),
        "seam": seam,
        "shoeProxyRanges": proxy_movements,
        "belowBaselineAlphaCount": [r["rawAlphaBelowNominalBaseline"]["countNonzero"] for r in evidence],
        "belowBaselineMaxAlpha": [r["rawAlphaBelowNominalBaseline"]["maxAlpha"] for r in evidence],
        "belowBaselineMaxBlackChannel": [r["rawAlphaBelowNominalBaseline"]["maxBlackCompositedChannel"] for r in evidence],
        "isolatedChromaCounts": [r["separatedChromaSignal"]["pixelCount"] for r in evidence],
        "generated": generated,
    }
    print("IDLE_FORENSICS_SUMMARY_START")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    print("IDLE_FORENSICS_SUMMARY_END")


if __name__ == "__main__":
    main()
