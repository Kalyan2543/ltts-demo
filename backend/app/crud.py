import bcrypt
from sqlalchemy.orm import Session

from .models import User, Category, Product, CartItem, Review, NewsletterSubscriber
from .schemas import UserCreate


def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))


def get_user_by_email(db: Session, email: str) -> User | None:
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, user_data: UserCreate) -> User:
    hashed = hash_password(user_data.password)
    db_user = User(
        email=user_data.email,
        password_hash=hashed,
        first_name=user_data.first_name,
        last_name=user_data.last_name,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def authenticate_user(db: Session, email: str, password: str) -> User | None:
    user = get_user_by_email(db, email)
    if not user:
        return None
    if not verify_password(password, user.password_hash):
        return None
    return user


# --- Product CRUD ---


def get_products(
    db: Session,
    featured: bool | None = None,
    trending: bool | None = None,
    category_id: int | None = None,
    search: str | None = None,
    skip: int = 0,
    limit: int = 20,
):
    query = db.query(Product, Category.name.label("category_name")).outerjoin(
        Category, Product.category_id == Category.id
    )
    if featured is not None:
        query = query.filter(Product.is_featured == featured)
    if trending is not None:
        query = query.filter(Product.is_trending == trending)
    if category_id is not None:
        query = query.filter(Product.category_id == category_id)
    if search:
        query = query.filter(Product.name.ilike(f"%{search}%"))
    rows = query.offset(skip).limit(limit).all()
    results = []
    for product, cat_name in rows:
        product.category_name = cat_name
        results.append(product)
    return results


def get_product_by_id(db: Session, product_id: int):
    row = (
        db.query(Product, Category.name.label("category_name"))
        .outerjoin(Category, Product.category_id == Category.id)
        .filter(Product.id == product_id)
        .first()
    )
    if row:
        product, cat_name = row
        product.category_name = cat_name
        return product
    return None


# --- Category CRUD ---


def get_categories(db: Session):
    return db.query(Category).all()


# --- Cart CRUD ---


def get_cart_items(db: Session, user_id: int):
    rows = (
        db.query(CartItem, Product)
        .outerjoin(Product, CartItem.product_id == Product.id)
        .filter(CartItem.user_id == user_id)
        .all()
    )
    results = []
    for cart_item, product in rows:
        cart_item.product = product
        results.append(cart_item)
    return results


def add_to_cart(db: Session, user_id: int, product_id: int, quantity: int):
    existing = (
        db.query(CartItem)
        .filter(CartItem.user_id == user_id, CartItem.product_id == product_id)
        .first()
    )
    if existing:
        existing.quantity += quantity
        db.commit()
        db.refresh(existing)
        return existing
    cart_item = CartItem(user_id=user_id, product_id=product_id, quantity=quantity)
    db.add(cart_item)
    db.commit()
    db.refresh(cart_item)
    return cart_item


def remove_from_cart(db: Session, cart_item_id: int, user_id: int):
    item = (
        db.query(CartItem)
        .filter(CartItem.id == cart_item_id, CartItem.user_id == user_id)
        .first()
    )
    if not item:
        return None
    db.delete(item)
    db.commit()
    return item


# --- Review CRUD ---


def get_reviews(db: Session, product_id: int):
    return db.query(Review).filter(Review.product_id == product_id).all()


# --- Newsletter CRUD ---


def subscribe_newsletter(db: Session, email: str):
    existing = db.query(NewsletterSubscriber).filter(NewsletterSubscriber.email == email).first()
    if existing:
        return None
    subscriber = NewsletterSubscriber(email=email)
    db.add(subscriber)
    db.commit()
    db.refresh(subscriber)
    return subscriber
