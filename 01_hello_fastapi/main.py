from fastapi import FastAPI

app = FastAPI(title="Hello FastAPI", description="A simple FastAPI application", version="1.0.0")

@app.get("/")
def home():
    return {"message": "Hello, FastAPI!", "code": 0}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello, {name}!", "code": 0}
    