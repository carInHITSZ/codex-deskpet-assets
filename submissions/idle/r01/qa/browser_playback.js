// Automated browser scheduling/paint test. Visual acceptance is expressly false.
"use strict";
const fs=require("fs"), path=require("path"),child=require("child_process");
const puppeteer=require("puppeteer-core");
(async()=>{
  const chrome=(process.env.CHROME_BIN||child.execFileSync("which",["google-chrome"]).toString().trim());
  const browser=await puppeteer.launch({headless:true,executablePath:chrome,args:["--no-sandbox","--disable-dev-shm-usage"]});
  try{
    const page=await browser.newPage();
    page.setDefaultTimeout(90000);
    await page.setViewport({width:1000,height:1150,deviceScaleFactor:1});
    const errors=[];
    page.on("pageerror",e=>errors.push(String(e)));
    const url="http://127.0.0.1:8765/submissions/idle/r01/qa/preview.html";
    await page.goto(url,{waitUntil:"networkidle0"});
    await page.evaluate(()=>loadFrames());
    const root=path.resolve("submissions/idle/r01/qa"),shots=path.join(root,"browser-captures");
    fs.mkdirSync(shots,{recursive:true});
    const records=[];
    for(const speed of [1,0.5,0.25]){
      const r=await page.evaluate(async s=>await window.playCycles(s,3),speed);
      const expected=Array.from({length:60},(_,i)=>i%20);
      r.sequenceCorrect=r.sequence.length===expected.length&&r.sequence.every((v,i)=>v===expected[i]);
      r.mechanicalOk=r.decoded===20&&r.paints===60&&!r.aborted&&r.sequenceCorrect;
      delete r.sequence;
      for(const [bg,name] of [["#101018","black"],["#ffffff","white"],["#d1b9e9","lilac"]]){
        await page.evaluate(b=>window.setBackdrop(b),bg);
        await page.screenshot({path:path.join(shots, "idle_"+String(speed).replace(".","p")+"_"+name+".png")});
      }
      records.push(r);
      process.stdout.write(JSON.stringify(r)+"\n");
    }
    const report={clip:"idle",revision:"r01",url,speedRecords:records,pageErrors:errors,
      allMechanicalOk:records.every(x=>x.mechanicalOk)&&errors.length===0,
      technicalInterpretation:"Three real browser playback loops at each requested speed, with observed DOM/canvas paints and timing; screenshots saved for separate human artistic inspection.",
      visualAcceptance:"not_checked",anatomicalContact:"not_checked",familyTransitions:"not_checked"};
    fs.writeFileSync(path.join(root,"browser-playback-current.json"),JSON.stringify(report,null,2)+"\n");
    console.log("PLAYBACK_AUDIT="+JSON.stringify(report));
    if(!report.allMechanicalOk)process.exitCode=1;
  }finally{await browser.close()}
})().catch(e=>{console.error(e);process.exitCode=1;});
