from fastapi import FastAPI

app = FastAPI()

@app.get("/api/")
def api_root():
    return {"msg": "FastAPI работает"}

@app.get("/api/hello")
def hello():
    return {"msg": "Привет с FastAPI!"}
