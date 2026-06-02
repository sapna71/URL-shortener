from fastapi import FastAPI

from app.api.urls import router as url_router
from app.api.analytics import router as analytics_router
from app.api.health import router as health_router

app=FastAPI()

app.include_router(url_router)
app.include_router(analytics_router)
app.include_router(health_router)
@app.get("/")
def root():
  return {"message:URL_Shortener running"}
