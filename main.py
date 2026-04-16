from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
import logging
import os
from pathlib import Path
from fastapi.staticfiles import StaticFiles

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory = BASE_DIR / "templates");
app.mount("/static", StaticFiles(directory= BASE_DIR /"static"), name="static") # For implementing css on template

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or your github pages URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(request = request, name = "temp.html")

@app.get("/test")
def test():
    return {"status": "success"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
  print("Incoming WS request")  # ADD THIS
  await websocket.accept()
  logger.info("WebSocket client connected")
  try:
    while True:
      data = await websocket.receive_text()
      logger.info(f"Received: {data}")
      await websocket.send_text(f"Hello over WebSocket!")
  except WebSocketDisconnect:
    logger.info("Client disconnected")