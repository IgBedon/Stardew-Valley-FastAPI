from typing import Optional
from pydantic import BaseModel

class Character(BaseModel):
    id: int | None = None
    name: str | None = None
    profession: str | None = None
    gender: str | None = None
    marriageable: bool = False
    image: str = "teste"
    
