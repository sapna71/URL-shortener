from fastapi import FastAPI

from app.api.urls include 
app=FastAPI()

@app.get("/")
def root():
  return {"message:URL_Shortener running"}
