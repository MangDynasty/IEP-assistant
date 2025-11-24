from typing import List, Optional
from sqlmodel import Session, select
from app.models.student import Student
from app.schemas.student import StudentCreate, StudentUpdate


def create_student(session: Session, student_in: StudentCreate) -> Student:
    student = Student.from_orm(student_in)
    session.add(student)
    session.commit()
    session.refresh(student)
    return student


def list_students(session: Session) -> List[Student]:
    return session.exec(select(Student)).all()


def get_student(session: Session, student_id: int) -> Optional[Student]:
    return session.get(Student, student_id)


def update_student(
    session: Session, student: Student, student_in: StudentUpdate
) -> Student:
    data = student_in.dict(exclude_unset=True)
    for key, value in data.items():
        setattr(student, key, value)
    session.add(student)
    session.commit()
    session.refresh(student)
    return student


def delete_student(session: Session, student: Student) -> None:
    session.delete(student)
    session.commit()
