from pydantic import BaseModel, Field
from typing import Optional


class User(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    username: str
    email: str
    first_name: str
    last_name: str                                                                                      
    date_of_birth: str
    address: str
    apt_number: Optional[str] = None