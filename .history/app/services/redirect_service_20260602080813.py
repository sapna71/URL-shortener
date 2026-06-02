from fastapi import HTTPException
from fastapi.responses import RedirectResponse

from app.models.url import URL

async def get_original_url(db, short_code):

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

    return RedirectResponse(url.long_url)