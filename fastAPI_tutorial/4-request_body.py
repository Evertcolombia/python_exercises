from fastapi import FastAPI
from pydantic import BaseModel

# create Data model, use standard Python types for all the attributes
# BaseModel is type pydantic
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

app = FastAPI ()

@app.post("/items")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item, q: str = None):
    #def create_item(item_id: int, item: Item)
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result
