from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://postgres:root@localhost:5432/url_shortener"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        def create_url(db, long_url, short_code):
    print("Saving URL:", long_url, short_code)

    url = URL(
        long_url=long_url,
        short_code=short_code
    )

    db.add(url)
    db.commit()
    db.refresh(url)

    print("Saved with ID:", url.id)

    return url