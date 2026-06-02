from fastapi import FastAPI

from app.api.health import router as health_router
from app.api.urls import router as url_router
from app.api.analytics import router as analytics_router


from app.core.database import Base, engine

Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(health_router)
app.include_router(analytics_router)
app.include_router(url_router)