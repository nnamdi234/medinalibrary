from pydantic import BaseModel, Field
from typing import Optional

class Book(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    title: str
    author: str
    year: int
    copies: int
    genre:  str
