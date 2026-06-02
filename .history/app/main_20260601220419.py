from fastapi import FastAPI

from 
app=FastAPI()

@app.get("/")
def root():
  return {"message:URL_Shortener running"}
