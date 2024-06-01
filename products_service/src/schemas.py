from pydantic import BaseModel


class Product(BaseModel):
    name: str
    description: str
    category_id: int
    price: float
    image: str
    creator: str


class ProductCreate(Product):
    pass


class Product(Product):
    id: int

    class Config:
        from_attributes = True


class CategoryBase(BaseModel):
    name: str
    description: str


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int

    class Config:
        from_attributes = True
