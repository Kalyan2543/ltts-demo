import re
from datetime import datetime

from pydantic import BaseModel, EmailStr, field_validator


class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str

    @field_validator("password")
    @classmethod
    def validate_password(cls, v: str) -> str:
        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters")
        if not re.search(r"[A-Z]", v):
            raise ValueError("Password must contain at least one uppercase letter")
        if not re.search(r"[a-z]", v):
            raise ValueError("Password must contain at least one lowercase letter")
        if not re.search(r"\d", v):
            raise ValueError("Password must contain at least one digit")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", v):
            raise ValueError("Password must contain at least one special character")
        return v


class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    created_at: datetime

    class Config:
        from_attributes = True


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str
    user: UserResponse


# --- Home Page Schemas ---


class CategoryResponse(BaseModel):
    id: int
    name: str
    description: str | None = None
    image_url: str | None = None

    class Config:
        from_attributes = True


class ProductResponse(BaseModel):
    id: int
    name: str
    description: str | None = None
    price: float
    image_url: str | None = None
    category_id: int | None = None
    rating: float = 0
    review_count: int = 0
    is_featured: bool = False
    is_trending: bool = False
    category_name: str | None = None

    class Config:
        from_attributes = True


class CartItemCreate(BaseModel):
    product_id: int
    quantity: int = 1


class CartItemResponse(BaseModel):
    id: int
    product_id: int
    quantity: int
    created_at: datetime
    product: ProductResponse | None = None

    class Config:
        from_attributes = True


class ReviewResponse(BaseModel):
    id: int
    user_id: int
    product_id: int
    rating: int
    comment: str | None = None
    created_at: datetime

    class Config:
        from_attributes = True


class NewsletterSubscribe(BaseModel):
    email: EmailStr


class NewsletterResponse(BaseModel):
    id: int
    email: str
    created_at: datetime

    class Config:
        from_attributes = True
