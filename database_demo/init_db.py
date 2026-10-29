import asyncio

import models  # noqa: F401  导入模型，确保表定义注册到 Base.metadata
from database import Base, engine


async def main():
  print("开始创建相关的表")
  async with engine.begin() as conn:
    await conn.run_sync(Base.metadata.create_all)
  await engine.dispose()
  print("相关的表已经创建成功")


if __name__ == "__main__":
  asyncio.run(main())
