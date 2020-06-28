from fastapi import FastAPI, Path, Body
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None


class User(BaseModel):
    username: str
    full_name: str = None


@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int = Path(..., title="item ID", ge=0, le=1000),
    q: str = None,
    item: Item = None,
    user: User
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item.tax:
        item = item.dict()
        tax = item["price"] * item["tax"]
        item.update({"total": tax})
        results.update({"item": item})
    results.update({"user": user})
    return results


@app.put("/users/{user_id}/items/{item_id}")
async def update_item(
    *,
    user_id : int,
    item_id: int,
    item: Item = Body(..., embed=False),
    user: User,
    importance: int = Body(..., gt=0),
    q: str = None
):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    
    if q:
        results.update({"q": q})
    return results

