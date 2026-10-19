// Genuine Chrome canvas schedule test only; human artistic acceptance remains NOT_CHECKED.
"use strict";
const fs=require("fs"),path=require("path"),child=require("child_process"),puppeteer=require("puppeteer-core");
(async()=>{
const exe=process.env.CHROME_BIN||child.execFileSync("which",["google-chrome"]).toString().trim();
const browser=await puppeteer.launch({headless:true,executablePath:exe,args:["--no-sandbox","--disable-dev-shm-usage"]});
try{
 const page=await browser.newPage();page.setDefaultTimeout(90000);
 await page.setViewport({width:1000,height:1150,deviceScaleFactor:1});
 const errors=[];page.on("pageerror",e=>errors.push(String(e)));
 const url="http://127.0.0.1:8765/submissions/blink/r01/qa/preview.html";
 await page.goto(url,{waitUntil:"networkidle0"});await page.evaluate(()=>loadFrames());
 const qa=path.resolve("submissions/blink/r01/qa");fs.mkdirSync(path.join(qa,"browser-captures"),{recursive:true});
 const records=[];
 for(const speed of [1,0.5,0.25]){
  const a=await page.evaluate(async s=>window.playCycles(s,3),speed);
  const expected=Array.from({length:51},(_,i)=>i%17);
  a.sequenceCorrect=a.sequence.length===51&&a.sequence.every((v,i)=>v===expected[i]);
  a.mechanicalOk=a.decoded===17&&a.paints===51&&a.sequenceCorrect&&!a.aborted;delete a.sequence;
  records.push(a);console.log("BLINK_SPEED_RECORD="+JSON.stringify(a));
  for(const [bg,label] of [["#12121b","black"],["#ffffff","white"],["#e2d5f4","lilac"]]){
   await page.evaluate(b=>window.setBackdrop(b),bg);
   const fname="blink-"+String(speed).replace(".","p")+"-"+label+".png";
   await page.screenshot({path:path.join(qa,"browser-captures",fname)});
  }
 }
 const summary={clip:"blink",revision:"r01",url,sourceFrames:17,uniqueSourceImages:9,speedRecords:records,
 pageErrors:errors,allMechanicalOk:records.every(r=>r.mechanicalOk)&&errors.length===0,
 artisticVisualAcceptance:"not_checked",anatomicalContact:"not_checked",familyTransitions:"not_checked",
 note:"3 real Chromium Canvas repetitions per speed; no visual art judgment"};
 fs.writeFileSync(path.join(qa,"browser-playback.json"),JSON.stringify(summary,null,2)+"\n");
 if(!summary.allMechanicalOk)process.exitCode=1;
}finally{await browser.close()}
})().catch(e=>{console.error(e);process.exitCode=1});
