from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None



app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


@app.get("/token/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}