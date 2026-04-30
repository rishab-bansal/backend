// Connecting with the backend using websocket
import { state } from "./sb_state.js";
const ws = new WebSocket('wss://rishab-bansal.onrender.com/ws');
// const ws = new WebSocket("ws://127.0.0.1:8000/ws")
let flag = true;
if(flag){
ws.onopen = () => {
  console.log("connected");
  ws.send(JSON.stringify({"message":'Hello from the client!'}));
}

ws.onmessage = (event) =>{
  if(ws.readyState === WebSocket.OPEN){

    const data = JSON.parse(event.data);
    if(data.message === "simdata"){
      // console.log(data.message)
      state.data = data.states;
      state.time = data.time;
    }
  }
}
}
ws.onerror = (e)=>console.log("Error",e);


// Simulation plays when the button is pressed
const startsim = document.getElementById("play");

startsim.addEventListener("click", function() {
  let ctxt = startsim.dataset.value;
  const data = {
    "message": "startsim",
    "context": ctxt
  }
  ws.send(JSON.stringify(data));
})