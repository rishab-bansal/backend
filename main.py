from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Backend showing the result!"}

@app.get("/test")
def test():
    return {"status": "success"}