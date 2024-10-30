from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
#asyncdef read_item(skip: int = 0, limit: int = 10):
async def read_item(skip: int = 0, limit: int = 2):
    return fake_items_db[skip : skip + limit] # slicing

# Request URL
# def read_item(0, 2)
# http://127.0.0.1:8000/items/?skip=0&limit=2


# -------------------------------------------------------------------------------------

# Required query parameters

@app.get("/items0/{item_id}")
async def read_item0(item_id: int, city: str):
    return {"item_id": item_id, "city": city}

# -------------------------------------------------------------------------------------

# Optional query parameters

@app.get("/items1/{item_id}")
async def read_item1(item_id: int, city: str | None = None):
    if city:
        return {"item_id": item_id, "city": city}
    return {"item_id": item_id}

# Request URL
# def read_item1(10, Pune)
# http://127.0.0.1:8000/items1/10?city=Pune


# -------------------------------------------------------------------------------------

# Query parameter type conversion

@app.get("/items2/{item_id}")
async def read_item2(item_id: int, city: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if city:
        item.update({"city": city})
    if not short:
        item.update( {"description": "This is amazing"} )
    return item

# Request URL

# def read_item2(10, true)
# http://127.0.0.1:8000/items2/10?short=true
# { "item_id": 10 }

# def read_item2(10, Pune, true)
# http://127.0.0.1:8000/items2/10?city=Pune&short=true
# { "item_id": 10, "city": "Pune" }

# def read_item2(10, false)
# http://127.0.0.1:8000/items2/10?short=false
# { "item_id": 10, "description": "This is amazing" }

# def read_item2(10, Pune, false)
# http://127.0.0.1:8000/items2/10?city=Pune&short=false
# { "item_id": 10, "city": "Pune", "description": "This is amazing" }



# -------------------------------------------------------------------------------------

# Multiple path and query parameters

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: int, city: str | None = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if city:
        item.update({"city": city})
    if not short:
        item.update( {"description": "This is an amazing item"} )
    return item

# Request URL

# def read_user_item(10, 11, _, true)
# http://127.0.0.1:8000/users/10/items/12?short=true
# { "item_id": 12, "owner_id": 10 }

# def read_user_item(10, 11, _, false)
# http://127.0.0.1:8000/users/10/items/12?short=false
# { "item_id": 12, "owner_id": 10, "description": "This is an amazing item" }

# def read_user_item(10, 11, Pune, true)
# http://127.0.0.1:8000/users/10/items/12?city=Pune&short=true
# { "item_id": 12, "owner_id": 10, "city": "Pune"}


# -------------------------------------------------------------------------------------

# Query Parameters and String Validations

from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results