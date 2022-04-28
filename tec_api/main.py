from fastapi import FastAPI, Depends, Path, Query
from schemas import Album
from schemas import AlbumOut
from schemas import AlbumOutNew
from schemas import AlbumName
from authentication import verify_token
import names

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/random_name")
async def root():
    return {"message": f"Hello {names.get_first_name()}"}


@app.get("/name/{name}")
async def root():
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
async def get_song(song_id: int = Path(..., title="The ID of the song", le=13)):
    return {"song_id": song_id, "song_name": song_db[song_id]}


@app.get("/album/{album_name}")
async def get_album(album_name: AlbumName):
    if album_name == AlbumName.folklore:
        return {"album_name": album_name, "year": 2020}
    if album_name.value == "evermore":
        return {"album_name": album_name, "year": 2020}
    return {"album_name": album_name, "year": 2021}


@app.get("/song_list")
async def get_song_list(skip: int = 0, limit: int = 10):
    return song_db[skip: skip + limit]


@app.post("/albums/")
async def create_album(album: Album):
    album_dict = album.dict()
    if album.discount:
        price_with_discount = album.price - album.discount * album.price * 0.01
        album_dict.update({"price_with_album": price_with_discount})
    return album_dict


@app.post("/albums/", response_model=AlbumOut)
async def create_album(album: Album):
    album_dict = album.dict()
    if album.discount:
        price_with_discount = album.price - album.discount * album.price * 0.01
        album_dict.update({"price_with_album": price_with_discount})
    return album_dict


@app.post("/albums/", response_model=AlbumOutNew)
async def create_album(album: Album):
    if album.discount:
        price_with_discount = album.price - album.discount * album.price * 0.01
        album = AlbumOutNew(**album.dict(), price_with_discount=price_with_discount)
    return album


@app.get("/check", dependencies=[Depends(verify_token)])
async def home():
    return {"detail": "Welcome home"}