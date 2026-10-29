
from fastapi import FastAPI, Depends, Query
import uvicorn

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello world"}

async def common_parameters(skip: int = Query(0, ge=0), limit: int = Query(10, le=60)):
    return {"skip": skip, "limit": limit}

@app.get("/items")
def read_items(commons: dict = Depends(common_parameters)):
    return commons


#
# if __name__ == "__main__":
#     uvicorn.run(app, host="localhost", port=8000)