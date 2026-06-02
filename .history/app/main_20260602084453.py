from fastapi import FastAPI

from app.models.url import URL
from app.core.database import Base, engine

from app.api.health import router as health_router
from app.api.url import router as url_router
from app.api.analytics import router as analytics_router

app.include_router(
    analytics_router
)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="URL Shortener"
)

app.include_router(health_router)
app.include_router(url_router)