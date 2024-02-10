#-----------------------------------------------#
from src import app
from src.tasks import check_service, get_merchants, add_data
#-----------------------------------------------#
import asyncio
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Request
#-----------------------------------------------#

# duh
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def read_root():
    return {"hellow": "dick"}

@app.post("/add_data")
async def add_mtx(req: Request):
    json_data = await req.json()

    if not json_data:
        return { "status": "failed" }

    asyncio.create_task(add_data(json_data))

    return { "status": "success" }

@app.post("/{pin}")
async def get_merchants(pin):
    asyncio.create_task(get_merchants(pin))

    return { "status": "success" }

@app.post("/check_av")
async def check_availability(req: Request):
    json_data = await req.json()

    if not json_data:
        return { "status": "failed" }

    asyncio.create_task(check_service(json_data))

    return { "status": "success"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, proxy_headers=True)
