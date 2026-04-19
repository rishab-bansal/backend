const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");
const ws = new WebSocket('wss://test-backend-7bl5.onrender.com/ws');

flag = true;
if(flag){
ws.onopen = () => {
  console.log("connected");
  ws.send('Hello from the client!');
}
}
ws.onerror = (e)=>console.log("Error",e);

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

function funct(){
    document.getElementById("canvas").margin = 2;
}
