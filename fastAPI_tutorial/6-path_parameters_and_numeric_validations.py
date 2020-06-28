from fastapi import FastAPI, Path, Query

# underhood path and query are just functions and not subclasses
app = FastAPI()

@app.get("/items/{item_id}")
async def read_items(
    item_id: int = Path(..., gt=0, le=1000),
    q: str = Query(None, alias="item-query")
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


@app.get("/users/items/{item_id}")
async def read_items(
    *,
    item_id: int = Path(..., title="The ID of the item to get"),
    q: str,
    size: float = Query(..., gt=0, lt=10.5)
):
    results = {"item_id": item_id, "size": size}
    if q:
        results.update({"q": q})
    return results

