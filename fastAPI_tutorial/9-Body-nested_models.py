from fastapi import FastAPI, Path
from pydantic import BaseModel, Field, HttpUrl
from typing import List, Set, Dict

app = FastAPI()

class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str = Field(..., max_length=20)
    description: str = None
    price: float = Field(..., gt=0.0)
    tax: float = None
    #tags: List[str] = [] repetitive items
    tags: Set[str] = set() #unique items
    #image: Image = None # use submodel as a type and nested models
    images: List[Image] = None


class Offer(BaseModel):
    name: str
    description: str = None
    price: float
    items: List[Item]


@app.post("/uses/{user_id}")
async def create_item(
        offer: Offer    
):
    return offer

@app.post("/item/{item_id}")
async def update_item(
    item_id: int = Path(..., gt=0, lt=10),
    item: Item = None
):
    results = {"item_id": item_id, "item": item}
    return results


@app.post("/images/multiple")
async def create_multiple_images(images: List[Image]):
    return images

@app.post("/index-weights/")
async def create_index_weights(weights: Dict[int, float]):
    return weights
