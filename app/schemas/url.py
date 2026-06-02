from pydantic import BaseModel

class CreateURLRequest(BaseModel):
  long_url:str



class URLResponse(BaseModel):
  short_url:str