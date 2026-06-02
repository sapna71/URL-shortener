from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.services.analytics_service import get_url_analytics
from app.core.database import get_db

router=APIRouter(tags=["analytics"])

@router.get("/analytics/{short_code}")
async def analytics(short)