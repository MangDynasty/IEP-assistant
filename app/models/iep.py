from datetime import date
from typing import Optional
from sqlmodel import SQLModel, Field, Relationship


class IEP(SQLModel, table=True):
    __tablename__ = "ieps"

    id: Optional[int] = Field(default=None, primary_key=True)
    student_id: int = Field(foreign_key="students.id")
    effective_date: date
    end_date: date
    status: str = Field(default="draft")  # draft / in_review / finalized

    # Simple text sections (non-AI Phase 1)
    present_levels: str = ""          # PLAAFP
    annual_goals: str = ""            # narrative goals section
    accommodations: str = ""          # accommodations/mods
    services: str = ""                # service delivery, minutes, etc.
    notes: str = ""                   # misc notes or meeting notes

    student: Optional["Student"] = Relationship(back_populates="ieps")


# back-populate relationship in student model
from app.models.student import Student  # noqa


Student.ieps = Relationship(back_populates="student")
