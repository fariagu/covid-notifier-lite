from typing import Optional
from fastapi import FastAPI
from html.parser import HTMLParser
from covid_notifier_lite.app.routes.hello import HelloRouter
from covid_notifier_lite.app.routes.covid import CovidRouter

app = FastAPI()
app.include_router(HelloRouter, tags=["Hello"], prefix="/hello")
app.include_router(CovidRouter, tags=["Covid"], prefix="/covid")

@app.get("/", tags=["Root"])
async def read_root():
    return { "message": "Hello World of Covid"}
