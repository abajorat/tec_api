from fastapi import FastAPI
import names
from pydantic import StrictStr

app = FastAPI()


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

@app.get("/songs/{song_id}")
async def get_song(song_id: int):
    return {"song_id": song_id, "song_name": song_db[song_id]}