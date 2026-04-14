from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or your github pages URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Backend showing"}

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