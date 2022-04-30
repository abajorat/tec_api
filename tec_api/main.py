from fastapi import FastAPI
import names
from pydantic import StrictStr
from fastapi import Path
from enum import Enum

app = FastAPI()


class AlbumName(str, Enum):
    folklore = "folklore"
    evermore = "evermore"
    red = "red"
    
    

# Path operation decorator
@app.get("/")
# Path operation function
async def root():
    return {"message": "Hello World and hello"}

  
@app.get("/random_name")
async def random_name():
    return {"message": f"Hello {names.get_first_name()}"}

@app.get("/name/{name}")
async def get_name(name: StrictStr):
    return {"message": f"Hello {name}"}

song_db = ["evermore", "willow", "champagne problems", "gold rush",
           "'tis the damn season'", "tolerate it", "no body no crime",
           "happiness", "dorothea", "coney island",
           "ivy", "cowboy like me", "long story short"]

@app.get("/songs/evermore")
async def get_evermore():
    return {"song_id": "0",
            "song_name": "evermore"}
    



@app.get("/songs/{song_id}")
async def get_song(song_id: int = Path(
  ...,  le=12)):
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