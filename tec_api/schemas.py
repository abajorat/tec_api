from pydantic import BaseModel, Field, confloat
from enum import Enum




class AlbumName(str, Enum):
    folklore = "folklore"
    evermore = "evermore"
    red = "red"


class Album(BaseModel):
    name: str
    description: str = None
    price: confloat(gt=0)
    discount: float = None


class AlbumOut(BaseModel):
    name: str
    description: str = None


class AlbumOutNew(BaseModel):
    name: str
    description: str = None
    price_with_discount: float
