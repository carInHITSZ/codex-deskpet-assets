#!/usr/bin/env python3
"""Read-only source art QA for blink; not new frame generation or artistic approval."""
import json,hashlib
from pathlib import Path
from datetime import datetime,timezone
import numpy as np
from PIL import Image,ImageDraw
repo=Path(__file__).resolve().parents[1]
qa=repo/"submissions/blink/r01/qa";qa.mkdir(parents=True,exist_ok=True)
tl=json.loads((repo/"groups/blink/current-timeline.json").read_text())
items=tl["frames"]
assert len(items)==17 and tl["plannedFrames"]==17
files=[];images=[];records=[]
for n,f in enumerate(items):
 assert f["sourceFrame"]==n
 path=repo/"groups/blink"/f["file"]; data=path.read_bytes()
 with Image.open(path) as im:
  fmt=im.format;im.load();picture=im.copy()
 errors=[]
 if fmt!="PNG" or picture.size!=(1024,1024) or picture.mode!="RGBA":errors.append("wrong_format_mode_or_size")
 if data[:8]!=b"\x89PNG\r\n\x1a\n" or data[24:26]!=bytes([8,6]):errors.append("not_rgba8_png_header")
 a=np.asarray(picture.getchannel("A"),dtype=np.uint8)
 b=picture.getchannel("A").point(lambda v:255 if v>8 else 0).getbbox()
 margins=[b[0],b[1],1024-b[2],1024-b[3]] if b else None
 if not margins or min(margins)<24:errors.append("unsafe_alpha_margin")
 if int(a.min())!=0 or int(a.max())!=255:errors.append("alpha_not_0_to_255")
 if not np.any((a>0)&(a<255)):errors.append("no_partial_alpha")
 files.append(f["file"]);images.append(picture)
 records.append({"frame":n,"assetId":f["assetId"],"path":"groups/blink/"+f["file"],
 "fileSha256":hashlib.sha256(data).hexdigest(),"size":list(picture.size),"mode":picture.mode,
 "alphaBBoxGt8":list(b) if b else None,"alphaMargins":margins,
 "reusedFrameNumbers":[j for j in range(n) if files[j]==files[n]],"failures":errors,
 "technicalOk":not errors,"visualAccepted":False})
def rgba_on(im,bg):
 canvas=Image.new("RGBA",im.size,tuple(bg)+(255,))
 return Image.alpha_composite(canvas,im).convert("RGB")
colors={"black":(0,0,0),"white":(255,255,255),"lilac":(226,213,244)}
outputs=[]
for region,rect in [("full",(260,236,770,915)),("face-codex-eyes",(365,250,655,482))]:
 w,h=rect[2]-rect[0],rect[3]-rect[1]
 for name,bg in colors.items():
  tw,th=w+24,h+25
  sheet=Image.new("RGB",(tw*5,th*4),(42,40,49));pen=ImageDraw.Draw(sheet)
  for i,im in enumerate(images):
   x,y=i%5*tw,i//5*th
   sheet.paste(rgba_on(im,bg).crop(rect),(x+12,y+2))
   pen.text((x+14,y+th-20),"%03d | %s | %s"%(i,region,name),fill=(236,235,239))
  fn="source-"+region+"-"+name+"-review.jpg"
  sheet.save(qa/fn,"JPEG",quality=75,optimize=True)
  outputs.append(fn)
def premul(im):
 a=np.asarray(im,dtype=np.float32)
 return a[:,:,:3]*(a[:,:,3:]/255.0)
base=premul(images[0]);differences=[]
for im in images:
 cur=premul(im)
 eyereg=np.abs(base[390:465,435:576]-cur[390:465,435:576])
 differences.append(round(float(eyereg.mean()),3))
palindrome=all(files[i]==files[-1-i] for i in range(17))
passTech=all(r["technicalOk"] for r in records)
report={"clip":"blink","revision":"r01","measuredUtc":datetime.now(timezone.utc).isoformat(),
 "sourceTimeline":"groups/blink/current-timeline.json","plannedFrames":17,
 "uniqueOriginalCandidateSourceFiles":len(set(files)),"palindromicExplicitSourceReuse":palindrome,
 "pixelIdenticalEndpoints":records[0]["fileSha256"]==records[-1]["fileSha256"],
 "originalsCopiedOrModified":False,"acceptedNewlyRedrawnFrames":0,"technicalPass":passTech,
 "eyeRegionPremultipliedAbsoluteDeltaFromFirst":differences,"frameEvidence":records,
 "reviewImages":outputs,"artAcceptance":False,
 "notChecked":["human_eyelid_artistic_motion","full_identity_and_Codex_topology",
 "true_ground_contact_landmarks_2px","same_pose_anatomical_scale_1percent",
 "three_speed_human_viewing","family_idle_blink","local_runtime"],
 "status":"candidate_source_technical_checked_visual_pending" if passTech else "candidate_source_technical_failed"}
(qa/"source-audit.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
print("BLINK_SOURCE_AUDIT="+json.dumps({"passed":passTech,"unique":len(set(files)),"slots":len(files),
 "symmetric":palindrome,"endpointsIdentical":report["pixelIdenticalEndpoints"],
 "errors":[r["frame"] for r in records if r["failures"]],"eyes":differences,"reviewImages":outputs}))
if not passTech:raise SystemExit(1)
