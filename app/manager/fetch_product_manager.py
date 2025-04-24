from sqlmodel import select, Session
from app.model.products_model import Product
from app.database.session import engine


def fetch_product(product_ids: list[str]):
    with Session(engine) as session:
        statement = (
            select(Product)
            .where(Product.id.in_(product_ids))
            .order_by(Product.product_rating.desc())
        )

        result = session.exec(statement).all()

        return result
