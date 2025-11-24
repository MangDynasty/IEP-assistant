from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from app.db.session import get_session
from app.schemas.student import StudentCreate, StudentRead, StudentUpdate
from app.services import student_service

router = APIRouter()


@router.post("/", response_model=StudentRead, status_code=status.HTTP_201_CREATED)
def create_student(
    student_in: StudentCreate,
    session: Session = Depends(get_session),
):
    return student_service.create_student(session, student_in)


@router.get("/", response_model=List[StudentRead])
def list_students(session: Session = Depends(get_session)):
    return student_service.list_students(session)


@router.get("/{student_id}", response_model=StudentRead)
def get_student(
    student_id: int,
    session: Session = Depends(get_session),
):
    student = student_service.get_student(session, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


@router.put("/{student_id}", response_model=StudentRead)
def update_student(
    student_id: int,
    student_in: StudentUpdate,
    session: Session = Depends(get_session),
):
    student = student_service.get_student(session, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student_service.update_student(session, student, student_in)


@router.delete("/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student(
    student_id: int,
    session: Session = Depends(get_session),
):
    student = student_service.get_student(session, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    student_service.delete_student(session, student)
    return None
