from fastapi import FastAPI

from app.api.urls import router as url_router
from app.api.analytics import router as analytics_router
from app.api.  
app=FastAPI()

@app.get("/")
def root():
  return {"message:URL_Shortener running"}
