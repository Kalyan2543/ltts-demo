from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float, ForeignKey, Text, UniqueConstraint
from sqlalchemy.sql import func

from .database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    password_hash = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    updated_at = Column(DateTime, nullable=False, server_default=func.now(), onupdate=func.now())


class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    image_url = Column(String)


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    image_url = Column(String)
    category_id = Column(Integer, ForeignKey("category.id"))
    rating = Column(Float, default=0)
    review_count = Column(Integer, default=0)
    is_featured = Column(Boolean, default=False)
    is_trending = Column(Boolean, default=False)
    created_at = Column(DateTime, nullable=False, server_default=func.now())


class CartItem(Base):
    __tablename__ = "cart_item"
    __table_args__ = (UniqueConstraint("user_id", "product_id", name="uq_cart_user_product"),)

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("product.id"), nullable=False)
    quantity = Column(Integer, default=1)
    created_at = Column(DateTime, nullable=False, server_default=func.now())


class Review(Base):
    __tablename__ = "review"
    __table_args__ = (UniqueConstraint("user_id", "product_id", name="uq_review_user_product"),)

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("product.id"), nullable=False)
    rating = Column(Integer, nullable=False)
    comment = Column(Text)
    created_at = Column(DateTime, nullable=False, server_default=func.now())


class NewsletterSubscriber(Base):
    __tablename__ = "newsletter_subscriber"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=func.now())


class HeroBanner(Base):
    __tablename__ = "hero_banner"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    subtitle = Column(String)
    image_url = Column(String)
    cta_text = Column(String)
    cta_link = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
