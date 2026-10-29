from pydantic import BaseModel
from fastapi import FastAPI
import uvicorn

from typing import Annotated

app = FastAPI()

class User(BaseModel):
  name: str
  age: int
  city: str | None = None

temp_user = {
  "name": "John",
  "age": "20",
  "city": "Beijing"
}

@app.get("/user")
def get_user():
  return { "user": User(**temp_user) }

@app.get("/say_hi")
def say_hi(name: Annotated[str, "The name to say hi to"]):
  return { "message": f"Hello, {name or 'World'}!" }

@app.get("/sync")
async def sync():
  return { "message": "Hello, World!" }

if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=8000)