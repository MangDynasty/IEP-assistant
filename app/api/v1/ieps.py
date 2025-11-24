from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from app.db.session import get_session
from app.schemas.iep import IEPCreate, IEPRead, IEPUpdate
from app.services import iep_service, student_service

router = APIRouter()


@router.post("/", response_model=IEPRead, status_code=status.HTTP_201_CREATED)
def create_iep(
    iep_in: IEPCreate,
    session: Session = Depends(get_session),
):
    # Ensure student exists (and later: belongs to current user)
    student = student_service.get_student(session, iep_in.student_id)
    if not student:
        raise HTTPException(status_code=400, detail="Student does not exist")
    return iep_service.create_iep(session, iep_in)


@router.get("/student/{student_id}", response_model=List[IEPRead])
def list_ieps_for_student(
    student_id: int,
    session: Session = Depends(get_session),
):
    return iep_service.list_ieps_for_student(session, student_id)


@router.get("/{iep_id}", response_model=IEPRead)
def get_iep(
    iep_id: int,
    session: Session = Depends(get_session),
):
    iep = iep_service.get_iep(session, iep_id)
    if not iep:
        raise HTTPException(status_code=404, detail="IEP not found")
    return iep


@router.put("/{iep_id}", response_model=IEPRead)
def update_iep(
    iep_id: int,
    iep_in: IEPUpdate,
    session: Session = Depends(get_session),
):
    iep = iep_service.get_iep(session, iep_id)
    if not iep:
        raise HTTPException(status_code=404, detail="IEP not found")
    return iep_service.update_iep(session, iep, iep_in)


@router.delete("/{iep_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_iep(
    iep_id: int,
    session: Session = Depends(get_session),
):
    iep = iep_service.get_iep(session, iep_id)
    if not iep:
        raise HTTPException(status_code=404, detail="IEP not found")
    iep_service.delete_iep(session, iep)
    return None
