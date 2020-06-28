from enum import Enum
from fastapi import FastAPI

class ModelName(str, Enum):
    elevert = "el_evert"
    eluxy = "el_luxy"
    laweed = "la_weed"

app = FastAPI()

@app.get("/model/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.elevert:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "el_luxy":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

