from fastapi import FastAPI, Depends,Path, Query
import names
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}