# app/db/session.py
from sqlmodel import SQLModel, create_engine, Session
from app.core.config import settings

engine = create_engine(settings.DATABASE_URL, echo=False)


def init_db() -> None:
    """Create tables (for dev; migrations later)."""
    import app.models.student  # noqa
    import app.models.iep      # noqa

    SQLModel.metadata.create_all(bind=engine)


def get_session():
    """FastAPI dependency for DB sessions."""
    with Session(engine) as session:
        yield session
