# Python
import os
import sys
from dotenv import dotenv_values

# Fast API
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware

# Pymongo
from pymongo import MongoClient

# Routers
from app import HOST, PORT, logger
from app.src.models.migrations import drop, migrate
from app.src.routers import history, payments, services, subscribers, teachers, staff

# Uvicorn
import uvicorn

CONFIG = dotenv_values(".env")

app = FastAPI()

origins = ["*"]

app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=False, allow_methods=["*"],
                   allow_headers=["*"],)


@app.on_event("startup")
def startup_db_client():
    """
    It creates a MongoDB client and connects to the database specified in the config file
    """
    mode = os.getenv("MODE")
    MONGO_DB_URL = CONFIG["MONGO_DB_URL"]
    MONGO_DB_PORT = CONFIG["MONGO_DB_PORT"]

    if mode == "PROD":
        logger.info(f"Mongo URL: db:{MONGO_DB_PORT}")
        app.mongodb_client = MongoClient("mongodb://db:27017")
    else:
        logger.info(f"Mongo URL: {MONGO_DB_URL}")
        app.mongodb_client = MongoClient(MONGO_DB_URL)

    app.database = app.mongodb_client[CONFIG["DB_NAME"]]
    logger.info("Successful connection to database")


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
app.include_router(teachers.router, prefix="/teacher")
app.include_router(staff.router, prefix="/staff")
app.include_router(services.router, prefix="/service")
app.include_router(payments.router, prefix="/payment")
app.include_router(history.router, prefix="/history")


if __name__ == '__main__':
    drop()
    migrate()
    logger.info(f"Database migration...")
    logger.info(f"App running...")
    uvicorn.run(app, host=HOST, port=PORT)
