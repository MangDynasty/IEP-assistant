# app/main.py
from fastapi import FastAPI
from app.api.v1 import students, ieps
from app.db.session import init_db

app = FastAPI(
    title="IEP Assistant",
    description="Phase 1: non-AI IEP drafting and management tool.",
    version="0.1.0",
)

app.include_router(students.router, prefix="/api/v1/students", tags=["students"])
app.include_router(ieps.router, prefix="/api/v1/ieps", tags=["ieps"])


@app.on_event("startup")
def on_startup() -> None:
    init_db()
