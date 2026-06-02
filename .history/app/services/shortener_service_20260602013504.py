from app.repositories.url_repository import create_url
import random
import string

async def create_short_url(db, long_url: str):
    short_code = "".join(
        random.choices(
            string.ascii_letters + string.digits,
            k=6
        )
    )

    url = create_url(
        db,
        long_url,
        short_code
    )

    return {
        "short_url": f"http://localhost:8000/r/{url.short_code}"
    }
async def create_short_url(db, long_url: str):
    return {
        "short_url": "http://localhost:8000/abc123"
    }