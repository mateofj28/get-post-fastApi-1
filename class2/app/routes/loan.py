from fastapi import APIRouter, Body, HTTPException, Path
from typing import List, Optional
from ..schemas.loan_schema import Loan

loan_route = APIRouter()

loan_db = []

# Create Loan
@loan_route.post("/", response_model=Loan)
def create_loan(loan: Loan = Body(...)):
    for existing_loan in loan_db:
        if existing_loan.id == loan.id:
            raise HTTPException(status_code=400, detail="Publisher with this ID already exists")
    loan_db.append(loan)
    return loan

# read Loan by id
@loan_route.get("/{loan_id}", response_model=Loan)
def read_loan(loan_id: int = Path(...)):
    for loan in loan_db:
        if loan.id == loan_id:
            return loan
    raise HTTPException(status_code=404, detail="Loan not found")

# List Loans
@loan_route.get("/", response_model=List[Loan])
def list_loans():
    return loan_db

# update Loan
@loan_route.put("/{Loan_id}", response_model=Loan)
def update_loan(loan_id: int, updated_loan: Loan = Body(...)):
    for index, loan in enumerate(loan_db):
        if loan.id == loan_id:
            loan_db[index] = updated_loan
            return updated_loan
    raise HTTPException(status_code=404, detail="loan not found")

# delete Loan by id
@loan_route.delete("/{loan_id}", response_model=Loan)
def delete_loan(loan_id: int = Path(...)):
    for index, loan in enumerate(loan_db):
        if loan.id == loan_id:
            removed_loan = loan_db.pop(index)
            return removed_loan
    raise HTTPException(status_code=404, detail="loan not found")
