from typing import Optional, List
from pydantic import BaseModel


class StudentBase(BaseModel):
    display_id: str
    first_name: str
    last_name: str
    grade_level: str


class StudentCreate(StudentBase):
    pass


class StudentUpdate(BaseModel):
    display_id: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    grade_level: Optional[str] = None


class StudentRead(StudentBase):
    id: int

    class Config:
        orm_mode = True
