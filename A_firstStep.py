from fastapi import FastAPI

app = FastAPI()

# @app.get("/")
# async def root():
#     return {"message": "Devashish"}

# *************************************************************************************

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# @app.get("/items")
# async def get_item():
#     return

class Item(BaseModel):
    name: str
    price: float
    tax: float | None = None


@app.post("/items/")
async def create_item(item: Item):
    return item

# Request URL
# http://127.0.0.1:8000/items/

# def create_item(phone, 5000, 50)
# { "name": "phone", "price": 5000, "tax": 50 }

# def create_item(phone, 5000, _)
# { "name": "phone", "price": 5000, "tax": null }


# ------------------------------------------------------------------------------------

# Request body + path parameters

@app.put("/items1/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.model_dump()}