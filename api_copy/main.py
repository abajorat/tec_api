from typing import Optional
from pydantic import BaseModel, Field
from fastapi import FastAPI, HTTPException, Depends, Request
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
    # price: float
    price: float = Field(..., gt=0, description="The price must be greater than zero")
    discount: Optional[float] = None


class AlbumOut(BaseModel):
    name: str
    description: Optional[str] = None


class AlbumOut2(BaseModel):
    name: str
    description: Optional[str] = None
    price_with_discount: float


def verify_token(req: Request):
    token = req.headers.get("Authorization", None)
    valid = token == 'BestPossiblePassword'
    if not valid:
        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )
    return True


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/albums/evermore")
async def get_evermore():
    return {"album_id": "1",
            "name": "Evermore"}


@app.get("/albums/{album_id}")
async def get_album(album_id: int):
    return {"album_id": album_id}


@app.get("/album_names/{album_name}")
async def get_album_name(album_name: AlbumName):
    if album_name == AlbumName.folklore:
        return {"album_name": album_name, "message": "This is me trying"}

    if album_name.value == "evermore":
        return {"album_name": album_name, "message": "Long Story Short"}

    return {"album_name": album_name, "message": "All too well"}


song_db = [{"song_name": "willow"}, {"song_name": "champagne problems"}, {"song_name": "gold rush"},
           {"song_name": "'tis the damn season'"}, {"song_name": "tolerate it"}, {"song_name": "no body no crime"},
           {"song_name": "happiness"}, {"song_name": "dorothea"}, {"song_name": "coney island"},
           {"song_name": "ivy"}, {"song_name": "cowboy like me"}, {"song_name": "long story short"}]


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


@app.post("/albums2/", response_model=AlbumOut)
async def create_album2(album: Album):
    album_dict = album.dict()
    if album.discount:
        price_with_discount = album.price - album.discount * album.price * 0.01
        album_dict.update({"price_with_album": price_with_discount})
    return album_dict


@app.post("/albums3/", response_model=AlbumOut2)
async def create_album3(album: Album):
    if album.discount:
        price_with_discount = album.price - album.discount * album.price * 0.01
        album = AlbumOut2(**album.dict(), price_with_discount=price_with_discount)
    return album


@app.get("/check", dependencies=[Depends(verify_token)])
async def home():
    return {"detail": "Welcome home"}