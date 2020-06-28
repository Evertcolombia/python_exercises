from fastapi import FastAPI, Body
from pydantic import BaseModel, Field

app = FastAPI()

class Item(BaseModel):
    name: str
    descripttion: str = Field(None, max_length=100)
    price: float = Field(..., gt=0)
    tax: float = None

@app.put("/items/{item_id}")
async def update_item(
    item_id: int,
    item: Item = Body(..., embed=True)
):
    results = {"item_id": item_id, "item": item}
    return results
