import random
import string

from sqlalchemy.orm import Session

from app.models.url import URL


def generate_short_code(length: int = 6) -> str:
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
    short_code = generate_short_code()

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