from fastapi import FastAPI

from app.urls
app=FastAPI()

@app.get("/")
def root():
  return {"message:URL_Shortener running"}
