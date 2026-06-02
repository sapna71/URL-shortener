from fastapi import FastAPI

from app.api.urls import router 
app=FastAPI()

@app.get("/")
def root():
  return {"message:URL_Shortener running"}
