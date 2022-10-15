from fastapi import FastAPI
import names
from pydantic import StrictStr
from enum import Enum

app = FastAPI()


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


@app.get("/songs")
async def get_song():
    return {"song_db": song_db}


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
