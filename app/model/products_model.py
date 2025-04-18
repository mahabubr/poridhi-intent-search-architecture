from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List


class Product(SQLModel, table=True):
    id: str = Field(primary_key=True)
    crawl_timestamp: str
    product_url: str
    product_name: str
    product_category_tree: str
    pid: str
    retail_price: float
    discounted_price: float
    image: str
    is_fk_advantage_product: bool
    description: Optional[str]
    product_rating: float
    overall_rating: float
    brand: str
    formatted_specifications: str
    product_category: str

    specifications: List["Specification"] = Relationship(back_populates="product")


class Specification(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    key: str
    value: str
    product_id: str = Field(foreign_key="product.id")

    product: Optional[Product] = Relationship(back_populates="specifications")
