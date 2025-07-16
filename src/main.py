from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/pingpong", response_class=PlainTextResponse)
async def pingpong():
    return "pong"

