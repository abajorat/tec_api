from typing import Optional
from pydantic import BaseModel, Field, confloat
from enum import Enum




class AlbumName(str, Enum):
    folklore = "folklore"
    evermore = "evermore"
    red = "red"


class Album(BaseModel):
    name: str
    # description: Optional[str] = None
    description: Optional[str] = Field(
        None, title="The description of the item", max_length=300
    )
    price: confloat(gt=0, description="The price must be greater than zero")
    discount: Optional[float] = None


class AlbumOut(BaseModel):
    name: str
    description: Optional[str] = None


class AlbumOutNew(BaseModel):
    name: str
    description: Optional[str] = None
    price_with_discount: float
