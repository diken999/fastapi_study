
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from typing import Any
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get("/")
def get_root():
    return {"message": "Hello, World!"}

@app.get("/name")
def get_name(first_name: str, last_name: str):
  return { "name": first_name.title() + " " + last_name.title() }

@app.get("/items/{item_id}")
def get_item(item_id: Any):
  return { "item_id": Any }

@app.get("/goods")
def get_current_user(goods_list: list[str]):
  return { "goods_list": goods_list }

@app.get("/users/{user_id}")
def get_user(user_id: str):
  return { "user_id": user_id }

@app.get("/say_hi")
def say_hi(name: str | None = None):
  return { "message": f"Hello, {name or 'World'}!" }

@app.get("/html", response_class=HTMLResponse)
def get_html():
   return """
   <html>
      <head>
         <title>HTML Response</title>
      </head>
      <body>
         <h1>Hello, World!</h1>
      </body>
   </html>
   """

@app.get("/file", response_class=FileResponse)
def get_file():
   file = "./file/logo.png"
   return FileResponse(file)

class User(BaseModel):
    username: str
    email: str
    full_name: str | None = None

# 自定义响应数据格式  response_model可以省略，直接返回 User 类
@app.get("/custom_response", response_model=User)
def get_custom_response():
    return User(
        username="john_doe",
        email="john@example.com",
        full_name="John Doe"
    )

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)