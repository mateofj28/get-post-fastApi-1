# main.py
from fastapi import FastAPI, Body
from models.user import User

app = FastAPI()

users_db = [
    User(id=1, name="Alice", email="alice@example.com", username="alice123", password="secret"),
    User(id=2, name="MAT", email="MAT@example.com", username="Mat1234", password="secret1"),
    User(id=3, name="fer", email="fer@example.com", username="fertt23", password="secret321"),
]

@app.get("/users/", response_model=list[User])
def get_users():
    return users_db

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/users/")
def create_user(user: User = Body(...)):
    return user
