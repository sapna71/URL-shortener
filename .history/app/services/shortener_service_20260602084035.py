import random
import string

from sqlalchemy.orm import Session

from app.models.url import URL


def generate_short_code(length=6):

    return "".join(
        random.choices(
            string.ascii_letters + string.digits,
            k=length
        )
    )


async def create_short_url(
    db: Session,
    long_url: str
):

    while True:

        short_code = generate_short_code()

        existing = (
            db.query(URL)
            .filter(URL.short_code == short_code)
            .first()
        )

        if not existing:
            break

    url = URL(
        long_url=long_url,
        short_code=short_code
    )

    db.add(url)
    db.commit()
    db.refresh(url)

    return {
        "short_code": short_code,
        "short_url": f"http://localhost:8000/{short_code}"
    }