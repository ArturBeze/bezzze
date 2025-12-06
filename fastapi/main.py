from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "FastAPI работает через Nginx HTTPS!"}

@app.get("/hello")
def hello():
    return {"status": "ok", "msg": "Привет с FastAPI!"}
