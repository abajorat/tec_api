from fastapi import FastAPI, Depends, Path, Query
import names
from .schemas import Album, AlbumOut, AlbumName
from .authentication import verify_token
from pydantic import StrictStr
app = FastAPI()


@app.get("/", dependencies=[Depends(verify_token)])
async def root():
    return {"message": "Hello World"}


@app.get("/random_name", dependencies=[Depends(verify_token)])
async def random_name():
    return {"message": f"Hello {names.get_first_name()}"}


@app.get("/name/{name}", dependencies=[Depends(verify_token)])
async def get_name(name: StrictStr):
    return {"message": f"Hello {name}"}


@app.get("/songs/evermore", dependencies=[Depends(verify_token)])
async def get_evermore():
    return {"song_id": "0",
            "song_name": "evermore"}


song_db = ["evermore", "willow", "champagne problems", "gold rush",
           "'tis the damn season'", "tolerate it", "no body no crime",
           "happiness", "dorothea", "coney island",
           "ivy", "cowboy like me", "long story short"]


@app.get("/songs/{song_id}", dependencies=[Depends(verify_token)])
async def get_song(song_id: int = Path(..., title="The ID of the song", le=12)):
    return {"song_id": song_id, "song_name": song_db[song_id]}


@app.get("/album/{album_name}", dependencies=[Depends(verify_token)])
async def get_album(album_name: AlbumName):
    if album_name == AlbumName.folklore:
        return {"album_name": album_name, "year": 2020}
    if album_name.value == AlbumName.evermore:
        return {"album_name": album_name, "year": 2020}
    return {"album_name": album_name, "year": 2021}


@app.get("/song_list", dependencies=[Depends(verify_token)])
async def get_song_list(skip: int = Query(..., le=12), limit: int = Query(10, le=12)):
    return song_db[skip: skip + limit]




albums = []


@app.post("/albums/", response_model=AlbumOut, dependencies=[Depends(verify_token)])
async def create_album(album: Album):
    album_dict = album.dict()
    albums.append(album)
    new_price = (album.price - album.discount * album.price * 0.01)
    album_dict.update({"new_price": new_price})
    return album_dict

@app.get("/albums/{album_id}", response_model=AlbumOut, dependencies=[Depends(verify_token)])
async def get_album(album_id: int):
    return albums[album_id]


@app.get("/check", dependencies=[Depends(verify_token)])
async def home():
    return {"detail": "Welcome home"}

import time
import asyncio
@app.get("/sync")
def home():
    time.sleep(5)
    return {"detail": "Welcome home"}

@app.get("/sync1")
def home():
    return {"detail": "Welcome home"}