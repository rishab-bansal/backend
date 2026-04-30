####### Libraries imported ####################
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
import logging
import asyncio
import os
from pathlib import Path
from fastapi.staticfiles import StaticFiles
import json
from projects.pend_on_cart.loop import simulate
################################################

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory = BASE_DIR / "templates")
app.mount("/static", StaticFiles(directory= BASE_DIR /"static"), name="static") # For implementing css on template

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or your github pages URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def land(request:Request):
   return templates.TemplateResponse(request=request, name = "home.html")

@app.get("/projects/self_balance/{page_name}")
def projects(request: Request, page_name: str):
    return templates.TemplateResponse(request = request, name = f"projects/self_balance/{page_name}.html", context = {"strategy":page_name})


@app.get("/{page_name}")
def home(request: Request, page_name:str):
###########################################
### Code added by copilot to remove the favicon error
###########################################
    if '.' in page_name:
        from fastapi.responses import HTMLResponse
        return HTMLResponse(status_code=404, content="File not found")
###########################################
    return templates.TemplateResponse(request = request, name = f"{page_name}.html", context = {"id":"Get me some", "title":"World"})


@app.get("/test")
def test():
    return {"status": "success"}



#############################################
##  Websocket connection with the frontend
#############################################
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
  print("Incoming WS request")  # Tells that a request is coming
  await websocket.accept()
  logger.info("WebSocket client connected") # Tells that the client is connected

  try:
    while True:
      data = await websocket.receive_text()
      msg = json.loads(data)
      logger.info(f"Received: {data}") # Prints the data sent by the client

###### Decoding what the client wants ########

      if msg["message"] == "startsim": # If the client wants to start a simulation
        # await simulate(websocket, msg["context"]) # Websocket can't accept another command until the simulation is complete
        asyncio.create_task(simulate(websocket, msg["context"])) # Simulation runs in the background and doesn't block the ws channel
      await websocket.send_json({"message":"Hello over WebSocket!"})

##### In-case the client gets disconnected #####
  except WebSocketDisconnect:
    logger.info("Client disconnected")