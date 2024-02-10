#-----------------------------------------------#
from src import app
#-----------------------------------------------#
from fastapi.middleware.cors import CORSMiddleware
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


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, proxy_headers=True)
