from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

from src.crud import (
    create_category, get_category, get_categories, update_category,
    delete_category, create_product, get_product, get_products,
    update_product, delete_product
)
from src.database import get_db
from src.schemas import Product, ProductCreate, Category, CategoryCreate


router = APIRouter()


@router.post("/categories/", response_model=Category)
def create_category_api(category: CategoryCreate, db: Session = Depends(get_db)):
    return create_category(db=db, category=category)


@router.get("/categories/{category_id}", response_model=Category)
def get_category_api(category_id: int, db: Session = Depends(get_db)):
    db_category = get_category(db=db, category_id=category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category


@router.get("/categories/", response_model=List[Category])
def get_categories_api(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_categories(db, skip=skip, limit=limit)


@router.put("/categories/{category_id}", response_model=Category)
def update_category_api(category_id: int, category: CategoryCreate, db: Session = Depends(get_db)):
    db_category = update_category(db=db, category_id=category_id, category_data=category)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category


@router.delete("/categories/{category_id}")
def delete_category_api(category_id: int, db: Session = Depends(get_db)):
    delete_category(db=db, category_id=category_id)
    return {"message": "Category deleted successfully"}


@router.post("/products/", response_model=Product)
def create_product_api(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db=db, product=product)


@router.get("/products/{product_id}", response_model=Product)
def get_product_api(product_id: int, db: Session = Depends(get_db)):
    db_product = get_product(db=db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product


@router.get("/products/", response_model=List[Product])
def get_products_api(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_products(db, skip=skip, limit=limit)


@router.put("/products/{product_id}", response_model=Product)
def update_product_api(product_id: int, product: ProductCreate, db: Session = Depends(get_db)):
    db_product = update_product(db=db, product_id=product_id, product_data=product)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product


@router.delete("/products/{product_id}")
def delete_product_api(product_id: int, db: Session = Depends(get_db)):
    delete_product(db=db, product_id=product_id)
    return {"message": "Product deleted successfully"}
