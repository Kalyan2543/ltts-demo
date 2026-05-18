from sqlalchemy.orm import Session

from .models import Category, Product, Review, HeroBanner


def seed_database(db: Session):
    # Only seed if tables are empty
    if db.query(Category).first() is not None:
        return

    categories = [
        Category(id=1, name="Electronics", description="Gadgets, devices, and tech accessories", image_url="https://picsum.photos/400/400?random=1"),
        Category(id=2, name="Fashion", description="Clothing, shoes, and accessories", image_url="https://picsum.photos/400/400?random=2"),
        Category(id=3, name="Home & Living", description="Furniture, decor, and home essentials", image_url="https://picsum.photos/400/400?random=3"),
        Category(id=4, name="Sports", description="Sports equipment and activewear", image_url="https://picsum.photos/400/400?random=4"),
        Category(id=5, name="Books", description="Fiction, non-fiction, and educational books", image_url="https://picsum.photos/400/400?random=5"),
        Category(id=6, name="Beauty", description="Skincare, makeup, and personal care", image_url="https://picsum.photos/400/400?random=6"),
    ]
    db.add_all(categories)
    db.commit()

    products = [
        Product(name="Wireless Bluetooth Headphones", description="Premium noise-cancelling headphones with 30-hour battery life", price=149.99, image_url="https://picsum.photos/400/400?random=10", category_id=1, rating=4.5, review_count=128, is_featured=True, is_trending=False),
        Product(name="Smart Watch Pro", description="Fitness tracker with heart rate monitor and GPS", price=299.99, image_url="https://picsum.photos/400/400?random=11", category_id=1, rating=4.3, review_count=89, is_featured=True, is_trending=True),
        Product(name="Portable Charger 20000mAh", description="Fast-charging power bank with dual USB ports", price=39.99, image_url="https://picsum.photos/400/400?random=12", category_id=1, rating=4.7, review_count=256, is_featured=False, is_trending=True),
        Product(name="Classic Leather Jacket", description="Genuine leather jacket with a modern slim fit", price=249.99, image_url="https://picsum.photos/400/400?random=13", category_id=2, rating=4.6, review_count=67, is_featured=True, is_trending=False),
        Product(name="Running Sneakers Ultra", description="Lightweight running shoes with responsive cushioning", price=129.99, image_url="https://picsum.photos/400/400?random=14", category_id=2, rating=4.4, review_count=193, is_featured=False, is_trending=True),
        Product(name="Minimalist Desk Lamp", description="LED desk lamp with adjustable brightness and color temperature", price=59.99, image_url="https://picsum.photos/400/400?random=15", category_id=3, rating=4.2, review_count=45, is_featured=True, is_trending=False),
        Product(name="Organic Cotton Throw Blanket", description="Soft and cozy blanket made from 100% organic cotton", price=79.99, image_url="https://picsum.photos/400/400?random=16", category_id=3, rating=4.8, review_count=112, is_featured=False, is_trending=True),
        Product(name="Yoga Mat Premium", description="Non-slip eco-friendly yoga mat with alignment lines", price=49.99, image_url="https://picsum.photos/400/400?random=17", category_id=4, rating=4.5, review_count=78, is_featured=True, is_trending=False),
        Product(name="Adjustable Dumbbell Set", description="Space-saving adjustable dumbbells from 5 to 50 lbs", price=399.99, image_url="https://picsum.photos/400/400?random=18", category_id=4, rating=4.6, review_count=54, is_featured=False, is_trending=True),
        Product(name="The Art of Programming", description="Comprehensive guide to modern software development practices", price=34.99, image_url="https://picsum.photos/400/400?random=19", category_id=5, rating=4.9, review_count=321, is_featured=True, is_trending=True),
        Product(name="Bestseller Mystery Novel", description="A gripping thriller that keeps you on the edge of your seat", price=14.99, image_url="https://picsum.photos/400/400?random=20", category_id=5, rating=4.3, review_count=189, is_featured=False, is_trending=False),
        Product(name="Vitamin C Serum", description="Brightening face serum with 20% Vitamin C and hyaluronic acid", price=29.99, image_url="https://picsum.photos/400/400?random=21", category_id=6, rating=4.7, review_count=234, is_featured=True, is_trending=True),
        Product(name="Natural Lip Balm Set", description="Organic lip balm collection with 6 flavors", price=12.99, image_url="https://picsum.photos/400/400?random=22", category_id=6, rating=4.4, review_count=98, is_featured=False, is_trending=False),
    ]
    db.add_all(products)
    db.commit()

    reviews = [
        Review(user_id=1, product_id=1, rating=5, comment="Best headphones I've ever owned! Crystal clear sound."),
        Review(user_id=1, product_id=3, rating=5, comment="Charges my phone 4 times. Great for travel."),
        Review(user_id=1, product_id=10, rating=5, comment="A must-read for any developer."),
        Review(user_id=1, product_id=12, rating=4, comment="Great serum, saw results in 2 weeks."),
        Review(user_id=1, product_id=8, rating=4, comment="Good quality mat, very comfortable for daily practice."),
    ]
    # Only add reviews if user with id=1 exists
    from .models import User
    if db.query(User).filter(User.id == 1).first():
        db.add_all(reviews)
        db.commit()

    # --- Hero Banners ---
    hero_banners = [
        HeroBanner(
            title="Summer Sale",
            subtitle="Up to 50% off on selected items",
            image_url="https://picsum.photos/1200/400?random=100",
            cta_text="Shop Now",
            cta_link="/products?featured=true",
            is_active=True,
        ),
        HeroBanner(
            title="New Arrivals",
            subtitle="Check out the latest trends in fashion and tech",
            image_url="https://picsum.photos/1200/400?random=101",
            cta_text="Explore",
            cta_link="/products?trending=true",
            is_active=True,
        ),
        HeroBanner(
            title="Free Shipping",
            subtitle="On all orders over $50 — limited time offer",
            image_url="https://picsum.photos/1200/400?random=102",
            cta_text="Learn More",
            cta_link="/products",
            is_active=True,
        ),
    ]
    db.add_all(hero_banners)
    db.commit()
