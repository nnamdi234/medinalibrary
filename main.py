from fastapi import FastAPI
from db import ping
from controller.book import router



app = FastAPI()
app.include_router(router)

@app.on_event("startup")
def on_start():
    ping()