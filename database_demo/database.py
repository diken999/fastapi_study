from datetime import datetime
from sqlalchemy import DateTime, Integer
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from config import settings

engine = create_async_engine(settings.database_url, echo=True)

class Base(DeclarativeBase):
  id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, sort_order=-1, comment="主键 id")
  create_time: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, comment="创建时间")