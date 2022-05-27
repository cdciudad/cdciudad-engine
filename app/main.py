# Fast API
from fastapi import FastAPI
from app.src.routers import subscribers, teachers

app = FastAPI()

# Routes
app.include_router(subscribers.router)
app.include_router(teachers.router)
