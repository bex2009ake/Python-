# uvicorn fast:app --reload
# from fastapi import FastAPI


# app = FastAPI()


# # @app.post("/")
# # def create_user_route(data):
# #    print(data) 
# #    return data

# @app.post("/create_user")
# def create_user_route(data):
#   print (data)
#   return data


from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.put("/")
async def create_item(item: Item):
    return item
