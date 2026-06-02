from fastapi import HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from app.models.url import URL
from app.core.redis import redis_client


async def get_original_url(
    db: Session,
    short_code: str
):
    # Check cache first
    cached_url = redis_client.get(short_code)

    if cached_url:
        print("Cache HIT")

        return RedirectResponse(
            url=cached_url,
            status_code=307
        )

    print("Cache MISS")

    # Query Postgres
    url = (
        db.query(URL)
        .filter(URL.short_code == short_code)
        .first()
    )

    if not url:
        raise HTTPException(
            status_code=404,
            detail="URL not found"
        )

    # Store in Redis for future requests
    redis_client.setex(
        short_code,
        3600,
        url.long_url
    )

    # Update analytics
    url.click_count += 1
    db.commit()

    return RedirectResponse(
        url=url.long_url,
        status_code=307
    )