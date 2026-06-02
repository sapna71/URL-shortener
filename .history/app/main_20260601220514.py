from fastapi import FastAPI

from app.api.urls import router as url_router
from  
app=FastAPI()

@app.get("/")
def root():
  return {"message:URL_Shortener running"}
