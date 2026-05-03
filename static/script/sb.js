import {state} from "./sb_state.js"

const canvas = document.getElementById("canvas_sb");
const ctx = canvas.getContext("2d");

/////////// Setting canvas dimensions //////////////
var cw = canvas.width;
var ch = canvas.height;
var px_per_meter = cw/10;
var ground;
var robot;

function resizeCanvas(){

    const dpr = window.devicePixelRatio || 1;
    let width;
    let height;
    if(document.documentElement.clientWidth > 1000){
        width = document.documentElement.clientWidth/2;
        height = width/2;
    }
    else{
        height = document.documentElement.clientHeight/2;
        width = document.documentElement.clientWidth/1.1;//height/2;
    }
    
    cw = width;
    ch = height;
    // Set CSS size (no overflow)
    canvas.style.width = width + "px";
    canvas.style.height = height + "px";
    
    // Set internal resolution (sharp rendering)
    canvas.width = width * dpr;
    canvas.height = height * dpr;
    
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    resetCanvasElements();
}

////////////////////////////////////////////////////
resizeCanvas();
window.addEventListener("resize", resizeCanvas)


function resetCanvasElements(){
    px_per_meter = cw/10;

    ground = {
        y: 0.5*ch,
    }
    
    robot = {
        cx: 0.5*cw,
        cs: 0.2*px_per_meter,
        get cy(){
            return ground.y - this.cs;
        },
        
        rl: 1*px_per_meter,
        ps: 0.1*px_per_meter,
        
        get px(){
            return this.cx
        },
        
        get py(){
            return ground.y - this.rl - this.cs
        },
        
    }
}


function drawRobot(){
    
    // cart
    ctx.beginPath();
    let ccx = robot.cx + px_per_meter*state.data[0];
    let ccy = robot.cy;
    ctx.arc(ccx, robot.cy, robot.cs, 0, Math.PI*2, false);
    ctx.fillStyle = "red";
    ctx.fill();
    
    // pendulum
    ctx.beginPath();
    let pcx = ccx - robot.rl*Math.sin(state.data[2]);
    let pcy = robot.cy - robot.rl*Math.cos(state.data[2]);
    ctx.arc(pcx, pcy, robot.ps, 0, Math.PI*2, false);
    ctx.fillStyle = "violet";
    ctx.fill();
    
    // connecting rod
    ctx.beginPath();
    ctx.moveTo(ccx, ccy);
    ctx.lineTo(pcx, pcy);
    // console.log(Math.sqrt((ccx - pcx)**2 + (ccy - pcy)**2));
    ctx.stroke();
}

function drawMarkers(){
    // Simulation Time
    let fontSize = px_per_meter*0.2;
    ctx.font = fontSize + 'px Arial';
    ctx.fillStyle = "black";
    ctx.fillText("Simulation Time: " + Math.round(state.time*100)/100, 0.5*cw, 0.9*ch);
    ctx.fillText(" sec", 0.69*cw, 0.9*ch);
    
    // Distance Markers
    const d = px_per_meter;
    const n = cw/d;
    
    ctx.beginPath();
    ctx.arc(0.5*cw, ground.y-robot.cs, 0.03*px_per_meter, 0, Math.PI*2, false);
    ctx.fillStyle = "blue";
    ctx.fill();
    
    ctx.beginPath();
    for(let i = 1; i < n; i++){
        ctx.arc(0.5*cw + i * d, ground.y-robot.cs, 0.03*px_per_meter, 0, Math.PI*2, false);
        ctx.arc(0.5*cw - i*d, ground.y-robot.cs, 0.03*px_per_meter, 0, Math.PI*2, false);
    }
    ctx.fillStyle = "green";
    ctx.fill()
}

function drawScene(){
    ctx.beginPath();
    ctx.moveTo(0, ground.y);
    ctx.lineTo(cw, ground.y);
    ctx.stroke();
    
    // Drawing robot
    drawRobot();
    
    // Drawing markers
    drawMarkers();
}


function update(){
    ctx.clearRect(0, 0, cw, ch);
    drawScene();
    requestAnimationFrame(update); // Recalls update function
}


update();