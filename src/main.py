from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
async def ping():
    return {
        "status": 10000,
        "msg": "success",
        "data": "pong"
    }

