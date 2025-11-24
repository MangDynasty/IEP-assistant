from datetime import date
from typing import Optional
from pydantic import BaseModel


class IEPBase(BaseModel):
    student_id: int
    effective_date: date
    end_date: date
    present_levels: str = ""
    annual_goals: str = ""
    accommodations: str = ""
    services: str = ""
    notes: str = ""


class IEPCreate(IEPBase):
    pass


class IEPUpdate(BaseModel):
    effective_date: Optional[date] = None
    end_date: Optional[date] = None
    present_levels: Optional[str] = None
    annual_goals: Optional[str] = None
    accommodations: Optional[str] = None
    services: Optional[str] = None
    notes: Optional[str] = None
    status: Optional[str] = None


class IEPRead(IEPBase):
    id: int
    status: str

    class Config:
        orm_mode = True
