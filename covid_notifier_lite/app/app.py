from typing import Optional
from fastapi import FastAPI
from app.routes.hello import HelloRouter

app = FastAPI()
app.include_router(HelloRouter, tags=["Hello"], prefix="/hello")

@app.get("/", tags=["Root"])
async def read_root():
    return { "message": "Hello World of Covid"}
