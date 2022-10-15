from pydantic import BaseModel, Field, confloat
from enum import Enum


class AlbumName(str, Enum):
    folklore = "folklore"
    evermore = "evermore"
    red = "red"
    
class Album(BaseModel):
    name: str
    description: str = 'Description missing'
    price: confloat(gt=0) 
    discount:float = 0

class AlbumOut(BaseModel):
    name: str
    description: str = None  
    new_price: float = None 