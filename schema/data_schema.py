from pydantic import BaseModel
from typing import Optional

class DataSchema(BaseModel):
    id: Optional[int]
    name: str
    desc: str

    class Config:
        orm_mode = True