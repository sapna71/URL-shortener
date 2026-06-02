from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.url import CreateURLRequest
from app.services.shortener_service import create_short_url
from app.core.database import get_db

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