# Fast API
from app import logger
from fastapi import FastAPI
from app.src.routers import subscribers

app = FastAPI()

# Routes
app.include_router(subscribers.router)

logger.info("Server is running in port 8000")
