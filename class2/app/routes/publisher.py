from fastapi import APIRouter, Body, HTTPException, Path
from typing import List, Optional
from ..schemas.publisher_schema import Publisher

publisher_route = APIRouter()

publisher_db = []

# Create publisher
@publisher_route.post("/", response_model=Publisher)
def create_publisher(publisher: Publisher = Body(...)):
    for existing_publisher in publisher_db:
        if existing_publisher.id == publisher.id:
            raise HTTPException(status_code=400, detail="Publisher with this ID already exists")
    publisher_db.append(publisher)
    return publisher

# read Publisher by id
@publisher_route.get("/{publisher_id}", response_model=Publisher)
def read_publisher(publisher_id: int = Path(...)):
    for publisher in publisher_db:
        if publisher.id == publisher_id:
            return publisher
    raise HTTPException(status_code=404, detail="Publisher not found")

# List Publishers
@publisher_route.get("/", response_model=List[Publisher])
def list_publishers():
    return publisher_db

# update Publisher
@publisher_route.put("/{publisher_id}", response_model=Publisher)
def update_Publisher(publisher_id: int, updated_Publisher: Publisher = Body(...)):
    for index, publisher in enumerate(publisher_db):
        if publisher.id == publisher_id:
            publisher_db[index] = updated_Publisher
            return updated_Publisher
    raise HTTPException(status_code=404, detail="Publisher not found")

# delete Publisher by id
@publisher_route.delete("/{publisher_id}", response_model=Publisher)
def delete_Publisher(publisher_id: int = Path(...)):
    for index, publisher in enumerate(publisher_db):
        if publisher.id == publisher_id:
            removed_publisher = publisher_db.pop(index)
            return removed_publisher
    raise HTTPException(status_code=404, detail="Publisher not found")
