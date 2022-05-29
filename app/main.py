# Fast API
from dotenv import dotenv_values
from fastapi import FastAPI, status
from pymongo import MongoClient
from app.src.routers import history, payments, services, staff, subscribers

config = dotenv_values(".env")

app = FastAPI()


@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(config["MONGODB_URL"])
    app.database = app.mongodb_client[config["DB_NAME"]]


@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()


@app.get(
    path="/",
    status_code=status.HTTP_200_OK,
    tags=["Home"]
)
def home():
    return "Welcome to 'Casa de la Ciudad' API 🚀"


# Routes
app.include_router(subscribers.router, prefix="/subscriber")
app.include_router(staff.router, prefix="/staff")
app.include_router(services.router, prefix="/service")
app.include_router(payments.router, prefix="/payment")
app.include_router(history.router, prefix="/history")
