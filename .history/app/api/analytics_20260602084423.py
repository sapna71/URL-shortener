from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.services.analytics_service import get_url_analytics

router = APIRouter(tags=["Analytics"])


@router.get("/analytics/{short_code}")
async def analytics(
    short_code: str,
    db: Session = Depends(get_db)
):
    return await get_url_analytics(
        db,
        short_code
    )