from pydantic import BaseModel

class Autor(BaseModel):
    id: int
    name: str
    biography: str