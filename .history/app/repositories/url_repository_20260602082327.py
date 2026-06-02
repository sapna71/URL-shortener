from sqlalchemy.orm import Session
from app.models.url import URL


def create_url(db, long_url, short_code):
    print("Saving:", long_url, short_code)

    url = URL(
        long_url=long_url,
        short_code=short_code
    )

    

    print("Saved ID:", url.id)

    return url


def get_by_short_code(db: Session, short_code: str):
    return (
        db.query(URL)
        .filter(URL.short_code == short_code)
        .first()
    )