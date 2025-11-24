from typing import Optional
from sqlmodel import SQLModel, Field


class Student(SQLModel, table=True):
    __tablename__ = "students"

    id: Optional[int] = Field(default=None, primary_key=True)
    # NOTE: Phase 1 is demo only – DO NOT use real student names/identifying info
    display_id: str = Field(index=True)  # e.g. "S-0001" pseudo-id
    first_name: str
    last_name: str
    grade_level: str  # e.g. "4", "9", "K"
    # Later: non-identifying demographic/context fields if needed
