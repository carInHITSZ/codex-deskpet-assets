#!/usr/bin/env python3
"""Deterministic PNG/alpha preflight. No art/playback acceptance is implied."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
from PIL import Image, ImageChops

def analyze(root: Path) -> dict:
    manifest = json.loads((root / "manifest.json").read_text(encoding="utf-8"))
    results = []
    prev_img = None
    for entry in manifest["frames"]:
        frame_path = root / entry["file"]
        native_path = root / entry["masterFile"]
        info = {
            "frame": entry["sourceFrame"],
            "path": entry["file"],
            "masterPath": entry["masterFile"],
            "technicalOk": False, "failures": [],
        }
        if not frame_path.is_file():
            info["failures"].append("missing_frame")
            results.append(info)
            continue
        data = frame_path.read_bytes()
        info["fileBytes"] = len(data)
        info["sha256"] = hashlib.sha256(data).hexdigest()
        try:
            with Image.open(frame_path) as original:
                info["sourceFormat"] = original.format
                original.load()
                im = original.copy()
        except Exception as e:
            info["failures"].append(f"unreadable_png:{type(e).__name__}")
            results.append(info)
            continue
        info["actualSize"] = list(im.size)
        info["mode"] = im.mode
        if info["sourceFormat"] != "PNG":
            info["failures"].append("not_png")
        if im.size != (1024, 1024):
            info["failures"].append("wrong_export_size")
        if im.mode != "RGBA":
            info["failures"].append("not_rgba")
        if im.mode == "RGBA":
            alpha = im.getchannel("A")
            hist = alpha.histogram()
            transparent = hist[0]
            partial = sum(hist[1:255])
            opaque = hist[255]
            info["alphaCount"] = {
                "zero": transparent, "partial": partial, "opaque": opaque,
                "min": alpha.getextrema()[0], "max": alpha.getextrema()[1],
            }
            bbox = alpha.point(lambda v: 255 if v > 8 else 0).getbbox()
            info["bboxAlphaGt8Exclusive"] = list(bbox) if bbox else None
            if bbox:
                left, top, right, bottom = bbox
                info["marginsAlphaGt8"] = {
                    "left": left, "top": top,
                    "right": 1024 - right, "bottom": 1024 - bottom,
                }
                if min(info["marginsAlphaGt8"].values()) < 24:
                    info["failures"].append("alpha_edge_margin_below_24px")
            else:
                info["failures"].append("no_visible_alpha_pixels")
            if transparent == 0 or transparent == im.width * im.height:
                info["failures"].append("no_mixed_visible_and_transparent_pixels")
            if prev_img is not None and im.size == prev_img.size:
                info["identicalPixelsToPreviousFrame"] = ImageChops.difference(im, prev_img).getbbox() is None
                if info["identicalPixelsToPreviousFrame"]:
                    info["failures"].append("identical_image_to_previous_frame")
            else:
                info["identicalPixelsToPreviousFrame"] = None
            prev_img = im
        if native_path.is_file():
            info["masterBytes"] = native_path.stat().st_size
            info["masterSha256"] = hashlib.sha256(native_path.read_bytes()).hexdigest()
            try:
                with Image.open(native_path) as orig_master:
                    info["masterSize"] = list(orig_master.size)
                    info["masterMode"] = orig_master.mode
            except Exception as e:
                info["failures"].append(f"master_unreadable:{type(e).__name__}")
        else:
            info["failures"].append("master_missing")
        info["technicalOk"] = len(info["failures"]) == 0
        results.append(info)
    return {
        "clip": manifest.get("clip"),
        "revision": manifest.get("revision"),
        "scope": "pixel_png_preflight_only_not_visual_or_playback_acceptance",
        "tested": len(results),
        "allTechnicalOk": len(results) == len(manifest["frames"]) and all(x["technicalOk"] for x in results),
        "failedFrames": [x["frame"] for x in results if not x["technicalOk"]],
        "notChecked": [
            "face_and_Codex_emblem_art_review", "contact_point_alignment",
            "playback_100_050_025", "loop_seam", "family_transitions", "runtime_integration",
        ],
        "frames": results,
    }

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()
    result = analyze(args.root)
    encoded = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        output = args.output if args.output.is_absolute() else args.root / args.output
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(encoded, encoding="utf-8")
    print(encoded)
    return 0 if result["allTechnicalOk"] else 1

if __name__ == "__main__":
    raise SystemExit(main())
