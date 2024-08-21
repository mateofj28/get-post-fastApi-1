from pydantic import BaseModel
from datetime import date

class Loan(BaseModel):
    id: int
    load_date: date
    due_date: date
    return_date: date
    status: str
    penalty: str
    book_id: int
    user_id: int