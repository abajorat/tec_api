from fastapi import FastAPI, Depends, Path, Query
import names
from .schemas import Album, AlbumOut, AlbumName
from .authentication import verify_token
from pydantic import StrictStr
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/random_name")
async def random_name():
    return {"message": f"Hello {names.get_first_name()}"}


@app.get("/name/{name}")
async def get_name(name: StrictStr):
    return {"message": f"Hello {name}"}


@app.get("/songs/evermore")
async def get_evermore():
    return {"song_id": "0",
            "song_name": "evermore"}


song_db = ["evermore", "willow", "champagne problems", "gold rush",
           "'tis the damn season'", "tolerate it", "no body no crime",
           "happiness", "dorothea", "coney island",
           "ivy", "cowboy like me", "long story short"]


@app.get("/songs/{song_id}")
async def get_song(song_id: int = Path(..., title="The ID of the song", le=12)):
    return {"song_id": song_id, "song_name": song_db[song_id]}


@app.get("/album/{album_name}")
async def get_album(album_name: AlbumName):
    if album_name == AlbumName.folklore:
        return {"album_name": album_name, "year": 2020}
    if album_name.value == AlbumName.evermore:
        return {"album_name": album_name, "year": 2020}
    return {"album_name": album_name, "year": 2021}


@app.get("/song_list")
async def get_song_list(skip: int = Query(..., le=12), limit: int = Query(10, le=12)):
    return song_db[skip: skip + limit]
#
#
# @app.post("/albums/", response_model=AlbumOut)
# async def create_album(album: Album):
#     album_dict = album.dict()
#     new_price = (album.price - album.discount * album.price * 0.01)
#     album_dict.update({"new_price": new_price})
#     return album_dict


@app.post("/albums/", response_model=AlbumOut)
async def create_album(album: Album):
    album_dict = album.dict()
    new_price = (album.price - album.discount * album.price * 0.01)
    album_dict.update({"new_price": new_price})
    return album_dict


@app.get("/check", dependencies=[Depends(verify_token)])
async def home():
    return {"detail": "Welcome home"}

@app.get("/sum/{v1}/{v2}")
async def sum(v1: int, v2: int):
    return {"resultado": v1+v2}
