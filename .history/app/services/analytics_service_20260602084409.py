from fastapi import HTTPException

from app.models.url import URL


async def get_url_analytics(
    db,
    short_code
):

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

    return {
        "short_code": url.short_code,
        "long_url": url.long_url,
        "clicks": url.click_count,
        "created_at": url.created_at
    }