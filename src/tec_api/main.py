from fastapi import FastAPI
import names
from pydantic import StrictStr
from enum import Enum
from pydantic import BaseModel, NegativeInt, PositiveInt, confloat, conlist, constr

app = FastAPI()


class Album(BaseModel):
    name: str
    description: str = "Default"
    price: confloat(gt=0) = "No price given"
    discount: float = None


class AlbumOut(BaseModel):
    name: str
    description: str = None
    new_price: float = None


class AlbumName(str, Enum):
    folklore = "folklore"
    evermore = "evermore"
    red = "red"


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/random_name")
async def random_name():
    return {"message": f"Hello {names.get_first_name()}"}


@app.get("/name/andre")
async def get_evermore():
    return {"Message": "Hello Hans"}


@app.get("/name/{name}")
async def get_name(name: StrictStr):
    return {"message": f"Hello {name}"}


song_db = [
    "evermore",
    "willow",
    "champagne problems",
    "gold rush",
    "'tis the damn season'",
    "tolerate it",
    "no body no crime",
    "happiness",
    "dorothea",
    "coney island",
    "ivy",
    "cowboy like me",
    "long story short",
]
album_dict = {}


@app.get("/songs")
async def get_song(skip: int = 0, limit: int = 10):
    return song_db[skip : skip + limit]


@app.get("/songs/{song_id}")
async def get_song(song_id: int):
    return {"song_id": song_id, "song_name": song_db[song_id]}


@app.get("/album/{album_name}")
async def get_album(album_name: AlbumName):
    if album_name == AlbumName.folklore:
        return {"album_name": album_name, "year": 2020}
    if album_name.value == "evermore":
        return {"album_name": album_name, "year": 2020}
    return {"album_name": album_name, "year": 2021}


@app.post("/albums", response_model=AlbumOut)
async def create_album(album: Album):
    album_dict = album.dict()
    new_price = album.price - album.discount * album.price
    album_dict.update({"new_price": new_price})
    return album_dict
