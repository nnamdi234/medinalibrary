from fastapi import FastAPI
from db import ping


app = FastAPI()

@app.on_event("startup")
def on_start():
    ping()