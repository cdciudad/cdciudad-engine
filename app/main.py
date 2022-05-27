# Fast API
from fastapi import FastAPI
from app.src.routers import administrative_staff, subscribers, teachers

app = FastAPI()

# Routes
app.include_router(subscribers.router)
app.include_router(teachers.router)
app.include_router(administrative_staff.router)
