from fastapi import FastAPI
import names
app = FastAPI()


# Path operation decorator
@app.get("/")
# Path operation function
async def root():
    return {"message": "Hello World and hello"}

  
@app.get("/random_name")
async def random_name():
    return {"message": f"Hello {names.get_first_name()}"}