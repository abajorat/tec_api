from pydantic import BaseModel, Field, confloat
from enum import Enum


class AlbumName(str, Enum):
    folklore = "folklore"
    evermore = "evermore"
    red = "red"


class Album(BaseModel):
    name: str
    description: str = 'No description given'
    price: confloat(gt=0)
    discount: float = None


class AlbumOut(BaseModel):
    name: str
    description: str = 'No description given'
    new_price: float
