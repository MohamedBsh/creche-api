from fastapi import FastAPI

from creche.db.engine import init_db
from creche.db.routers import creches, children, caregivers, enrollments, parents

app = FastAPI()

DB_FILE = "sqlite:///creche.db"

@app.on_event("startup")
async def startup_event():
    init_db(DB_FILE)

app.include_router(creches.router)
app.include_router(children.router)
app.include_router(caregivers.router)
app.include_router(enrollments.router)
app.include_router(parents.router)