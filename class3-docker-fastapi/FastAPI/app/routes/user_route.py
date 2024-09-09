from fastapi import APIRouter, Body
from models.user import User

from database import UserModel

user_route = APIRouter()


@user_route.get("/users")
def get_users():
    # Logic to fetch and return all users
    pass


@user_route.get("/users/{user_id}")
def get_user(user_id: int):
    # Logic to fetch and return a specific user by ID
    pass


@user_route.post("/users")
def create_user(user: User = Body(...)):
    UserModel.create(username=user.username, email=user.email, password=user.password)
    return user


@user_route.put("/users/{user_id}")
def update_user(user_id: int, user_data: dict):
    # Logic to update a user by ID
    pass


@user_route.delete("/users/{user_id}")
def delete_user(user_id: int):
    # Logic to delete a user by ID
    pass