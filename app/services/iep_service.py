from typing import List, Optional
from sqlmodel import Session, select
from app.models.iep import IEP
from app.schemas.iep import IEPCreate, IEPUpdate


def create_iep(session: Session, iep_in: IEPCreate) -> IEP:
    iep = IEP.from_orm(iep_in)
    session.add(iep)
    session.commit()
    session.refresh(iep)
    return iep


def list_ieps_for_student(session: Session, student_id: int) -> List[IEP]:
    statement = select(IEP).where(IEP.student_id == student_id)
    return session.exec(statement).all()


def get_iep(session: Session, iep_id: int) -> Optional[IEP]:
    return session.get(IEP, iep_id)


def update_iep(session: Session, iep: IEP, iep_in: IEPUpdate) -> IEP:
    data = iep_in.dict(exclude_unset=True)
    for key, value in data.items():
        setattr(iep, key, value)
    session.add(iep)
    session.commit()
    session.refresh(iep)
    return iep


def delete_iep(session: Session, iep: IEP) -> None:
    session.delete(iep)
    session.commit()
