from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def root():
  print{"message:URL_Shortener running"}
