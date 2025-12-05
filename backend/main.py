from fastapi import FastAPI

app = FastAPI()

@app.get("/api/")
def root():
    return {"message": "FastAPI работает через Nginx HTTPS!"}

@app.get("/api/hello")
def hello():
    return {"status": "ok", "msg": "Привет с FastAPI!"}
