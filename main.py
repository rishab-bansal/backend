from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Backend is on work!"}

@app.get("/test")
def test():
    return {"status": "success"}