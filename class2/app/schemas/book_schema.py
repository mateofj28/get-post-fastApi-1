from pydantic import BaseModel
from datetime import date


class Book(BaseModel):
    id: int
    title: str
    isbn: str
    publication_date: date
    author_id: int
    publisher_id: int
    category_id: int