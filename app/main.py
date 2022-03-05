# Fast API
from fastapi import FastAPI
from app.email.service import send_email
from app.routers import subscribers

app = FastAPI()
send_email()

# Routes
app.include_router(subscribers.router)
