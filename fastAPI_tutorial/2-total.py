from enum import Enum
from fastapi import FastAPI

class ModelName(str, Enum):
    elevert = "el_evert"
    eluxy = "el_luxy"
    laweed = "la_weed"

app = FastAPI()

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the_current_user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.elevert:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "el_luxy":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

