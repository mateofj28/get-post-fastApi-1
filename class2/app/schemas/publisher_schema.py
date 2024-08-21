from pydantic import BaseModel

class Publisher(BaseModel):
    id: int
    name: str
    address: str