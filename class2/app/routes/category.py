from fastapi import APIRouter, Body, HTTPException, Path
from typing import List, Optional
from ..schemas.category_schema import Category

category_route = APIRouter()

category_db = []

# Create Loan
@category_route.post("/", response_model=Category)
def create_category(category: Category = Body(...)):
    for existing_category in category_db:
        if existing_category.id == category.id:
            raise HTTPException(status_code=400, detail="Category with this ID already exists")
    category_db.append(category)
    return loan

# read Loan by id
@category_route.get("/{category_id}", response_model=Category)
def read_loan(category_id: int = Path(...)):
    for loan in category_db:
        if loan.id == category_id:
            return loan
    raise HTTPException(status_code=404, detail="Loan not found")

# List Loans
@category_route.get("/", response_model=List[Category])
def list_Categories():
    return category_db

# update Loan
@category_route.put("/{category_id}", response_model=Category)
def update_category(category_id: int, updated_category: Category = Body(...)):
    for index, loan in enumerate(category_db):
        if category.id == category_id:
            category_db[index] = updated_category
            return updated_category
    raise HTTPException(status_code=404, detail="Category not found")

# delete Loan by id
@category_route.delete("/{category_id}", response_model=Category)
def delete_category(category_id: int = Path(...)):
    for index, category in enumerate(category_db):
        if category.id == category_id:
            removed_category = category_db.pop(index)
            return removed_category
    raise HTTPException(status_code=404, detail="Category not found")
