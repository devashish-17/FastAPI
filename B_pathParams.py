from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Path Parameters"}


# Path Parameters

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}


# Path Parameters with types

@app.get("/items1/{item_id}")
async def read_item1(item_id: int):
    return {"item_id": item_id}

