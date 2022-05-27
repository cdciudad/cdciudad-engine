# Fast API
from fastapi import FastAPI, status
from app.src.routers import staff, subscribers

app = FastAPI()


@app.get(
    path="/",
    status_code=status.HTTP_200_OK,
    tags=["Home"]
)
def home():
    return "Welcome to 'Casa de la Ciudad' API 🚀"


# Routes
app.include_router(subscribers.router)
app.include_router(staff.router, prefix="/staff")
