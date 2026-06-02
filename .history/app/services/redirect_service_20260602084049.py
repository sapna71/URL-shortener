from fastapi import HTTPException
from fastapi.responses import RedirectResponse

from sqlalchemy.orm import Session

from app.models.url import URL


async def get_original_url(
    db: Session,
    short_code: str
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

    return RedirectResponse(
        url=url.long_url
    )