from sqlalchemy import String, Integer, Boolean, Numeric, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from database import Base
from decimal import Decimal

class Category(Base):
  __tablename__ = "categories"
  __table_args__ = { "comment": "商品分类表" }

  name: Mapped[str] = mapped_column(String(50), unique=True, comment="分类名称")


class Product(Base):
  __tablename__ = "products"
  __table_args__ = { "comment": "商品表" }

  category_id: Mapped[int] = mapped_column(
    ForeignKey("categories.id"), nullable=False, comment="所属分类 ID"
  )
  name: Mapped[str] = mapped_column(String(50), nullable=False, comment="商品名称")
  price: Mapped[Decimal]  = mapped_column(Numeric(8, 2), nullable=False, comment="商品单价（元）")
  stock: Mapped[int] = mapped_column(Integer, nullable=False, default=0, comment="商品库存")
  shelf_status: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True, comment="是否上架")