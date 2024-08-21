from fastapi import APIRouter, Body, HTTPException, Path
from typing import List, Optional
from ..schemas.book_schema import Book

book_route = APIRouter()

book_db = []

# Create Book
@book_route.post("/", response_model=Book)
def create_book(book: Book = Body(...)):
    for existing_book in book_db:
        if existing_book.id == book.id:
            raise HTTPException(status_code=400, detail="Book with this ID already exists")
    book_db.append(book)
    return book

# read Book by id
@book_route.get("/{book_id}", response_model=Book)
def read_book(book_id: int = Path(...)):
    for book in book_db:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

# List Books
@book_route.get("/", response_model=List[Book])
def list_books():
    return book_db

# update Book
@book_route.put("/{book_id}", response_model=Book)
def update_book(book_id: int, updated_book: Book = Body(...)):
    for index, book in enumerate(book_db):
        if book.id == book_id:
            book_db[index] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")

# delete Book by id
@book_route.delete("/{book_id}", response_model=Book)
def delete_book(book_id: int = Path(...)):
    for index, book in enumerate(book_db):
        if book.id == book_id:
            removed_book = book_db.pop(index)
            return removed_book
    raise HTTPException(status_code=404, detail="Book not found")
