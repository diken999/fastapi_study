from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from fastapi import FastAPI
import uvicorn

app = FastAPI()

ASYNC_DATABASE_URL = "mysql+asyncmy://root:12345678@localhost:3306/school.db"

# 创建异步引擎
async_engine = create_async_engine(
  ASYNC_DATABASE_URL,
  echo=True, # 可选：输出 SQL 日志
  pool_size=5, # 可选：连接池大小 
  max_overflow=10, # 可选：连接池最大溢出数
)

class Base(DeclarativeBase):
    pass

class Book(Base):
    __tablename__ = "book"

    id: Mapped[int] = mapped_column(primary_key=True, comment="书籍Id")
    bookname: Mapped[str] = mapped_column(comment="书籍名称")
    

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)