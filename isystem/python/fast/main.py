# uvicorn main:app --reload
from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get ("/")
def read_root ():
 return {"Hello": "World"}


@app.post("/upload/")
async def create_upload_file(data):
  return data