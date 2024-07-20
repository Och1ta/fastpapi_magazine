from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Category(Base):
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = Column(String(100), nullable=False)
    description: Mapped[str] = Column(String(250), nullable=False)

    products: Mapped[list["Product"]] = relationship("Product", back_populates="category")

    def __repr__(self):
        return f"<Category(name='{self.name}', description='{self.description}')>"


class Product(Base):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = Column(String(100), nullable=False)
    description: Mapped[str] = Column(String(250), nullable=False)
    category_id: Mapped[int] = Column(Integer, ForeignKey('categories.id'))
    category: Mapped[Category] = relationship("Category", back_populates="products")
    price: Mapped[float] = Column(Float, nullable=False)
    image: Mapped[str] = Column(String(250), nullable=False)
    creator: Mapped[str] = Column(String(50), nullable=False)

    def __repr__(self):
        return f"<Product(name='{self.name}',description='{self.description}', price='{self.price}', creator='{self.creator}')>"
