from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

app = FastAPI()

itemdb = []
class Item(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    price: float
    created_at: datetime = datetime.now()

@app.get("/")
async def get_items():
    return itemdb

@app.post("/")
def add_item(item: Item):
    itemdb.append(item.dict())
    return itemdb[-1]

@app.get("/{item_id}")
def get_item(item_id: int):
    item = item_id - 1
    return itemdb[item]

@app.post("/{item_id}/update")
def update_item(item_id: int, item: Item):
    itemdb[item_id] = item
    return {"message": "Item has been updated succesfully"}


@app.delete("/{item_id}/delete")
def delete_item(item_id: int):
    itemdb.pop(item_id-1)
    return {"message": "Item has been deleted succesfully"}