import uvicorn

def start():
    uvicorn.run("backend.app.app:app", host="0.0.0.0", port=8000, reload=True)
