from fastapi import FastAPI

from app.core.database import Base, engine
from app.models.url import URL

from app.api.health import router as health_router
from app.api.urls import router as url_router
from app.api.analytics import router as analytics_router


Base.metadata.create_all(bind=engine)

# Create FastAPI app FIRST
app = FastAPI(
    title="URL Shortener"
)

# THEN register routers
app.include_router(health_router)
app.include_router(url_router)
app.include_router(analytics_router)