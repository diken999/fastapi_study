
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.middleware("http")
async def middleware1(request, call_next):
    print("中间件 1 开始")
    response = await call_next(request)
    print("中间件 1 结束")
    return response

@app.middleware("http")
async def middleware2(request, call_next):
    print("中间件 2 开始")
    response = await call_next(request)
    print("中间件 2 结束")
    return response


@app.get("/")
def root():
    print("根路由处理函数")
    return {"message": "Hello world"}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000) 