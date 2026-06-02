import random
import string

from app.repositories.url_repository import create_url


async def create_short_url(db, long_url: str):
    short_code = "".join(
        random.choices(
            string.ascii_letters + string.digits,
            k=6
        )
    )

    url = create_url(
        db=db,
        long_url=long_url,
        short_code=short_code
    )

    return {
        "short_url": f"http://localhost:8000/r/{url.short_code}"
    }