
from fastapi import FastAPI, HTTPException
import uvicorn

app = FastAPI()

# 按 id 查询
@app.get("/id/{id}")
def get_id(id: int):
    if id in range(1, 5):
        return {"id": id}
    raise HTTPException(status_code=404, detail="Item not found")

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)