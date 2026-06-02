from fastapi import HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from app.models.url import URL


async def get_original_url(
    db: Session,
    short_code: str
):
    # Find URL in database
    url = (
        db.query(URL)
        .filter(URL.short_code == short_code)
        .first()
    )

    # If URL does not exist
    if not url:
        raise HTTPException(
            status_code=404,
            detail="URL not found"
        )

    # Increment click count
    url.click_count += 1

    # Save updated count
    db.commit()

    # Redirect user
    return RedirectResponse(
        url=url.long_url,
        status_code=307
    )