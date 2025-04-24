from sqlmodel import SQLModel, Field
from typing import Optional


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
    description: Optional[str] = None
    product_rating: float
    overall_rating: float
    brand: str
    formatted_specifications: str
    product_category: str
