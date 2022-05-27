# Fast API
from dotenv import dotenv_values
from fastapi import FastAPI, status
from pymongo import MongoClient
from app.src.routers import staff, subscribers

config = dotenv_values(".env")

app = FastAPI()

'''
@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(config["MONGO_DB_URL"])
    app.database = app.mongodb_client[config["DB_NAME"]]


@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()'''


@app.get(
    path="/",
    status_code=status.HTTP_200_OK,
    tags=["Home"]
)
def home():
    return "Welcome to 'Casa de la Ciudad' API 🚀"


# Routes
app.include_router(subscribers.router, prefix="/subscribers")
app.include_router(staff.router, prefix="/staff")
