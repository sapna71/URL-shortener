from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.url import CreateURLRequest
from app.services.shortener_service import create_short_url
from app.services.redirect_service import get_original_url

router = APIRouter(tags=["URLs"])


@router.post("/urls/shorten")
async def shorten_url(
    request: CreateURLRequest,
    db: Session = Depends(get_db)
):
    return await create_short_url(
        db,
        request.long_url
    )


@router.get("/{short_code}")
async def redirect_url(
    short_code: str,
    db: Session = Depends(get_db)
):
    return await get_original_url(
        db,
        short_code
    )