from fastapi import APIRouter, Body, HTTPException, Path
from typing import List, Optional
from ..schemas.user_schema import User

user_route = APIRouter()

# @user_route.post("/")
# def create_users(user: User = Body(...)):
#     try:
#         return user
#     except Exception as e:
#         print(e)
#         return {"error": str(e)}


users_db = []

# Create user
@user_route.post("/", response_model=User)
def create_user(user: User = Body(...)):
    for existing_user in users_db:
        if existing_user.id == user.id:
            raise HTTPException(status_code=400, detail="User with this ID already exists")
    users_db.append(user)
    return user

# read user by id
@user_route.get("/{user_id}", response_model=User)
def read_user(user_id: int = Path(...)):
    for user in users_db:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

# List users
@user_route.get("/", response_model=List[User])
def list_users():
    return users_db

# update user
@user_route.put("/{user_id}", response_model=User)
def update_user(user_id: int, updated_user: User = Body(...)):
    for index, user in enumerate(users_db):
        if user.id == user_id:
            users_db[index] = updated_user
            return updated_user
    raise HTTPException(status_code=404, detail="User not found")

# delete user by id
@user_route.delete("/{user_id}", response_model=User)
def delete_user(user_id: int = Path(...)):
    for index, user in enumerate(users_db):
        if user.id == user_id:
            removed_user = users_db.pop(index)
            return removed_user
    raise HTTPException(status_code=404, detail="User not found")
