from fastapi import FastAPI

from app.
app=FastAPI()

@app.get("/")
def root():
  return {"message:URL_Shortener running"}
