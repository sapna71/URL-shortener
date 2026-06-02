from fastapi import FastAPI

from app.api.urls import
app=FastAPI()

@app.get("/")
def root():
  return {"message:URL_Shortener running"}
