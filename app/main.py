# Fast API
from fastapi import FastAPI
from app.src.routers import subscribers

app = FastAPI()

# Routes
app.include_router(subscribers.router)
