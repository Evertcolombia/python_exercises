from typing import List
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
#async def read_items(q: str = None):
async def tead_items(q: str = Query(None, min_length=3, max_length=50, regex="^fixedquery$")):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@app.get("/items/{item_id}")
async def read_items(item_id: int, q: str = Query(..., min_length=3)):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

@app.get("/users/{user_id}/items/{item_id}")
async def read_items(user_id: int, item_id: int, q: List[str] = Query(["foo", "bar"])):
    results = {"user_id": user_id, "item_id": item_id}
    if q:
        results.update({"q": q})
    return results
