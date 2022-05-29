# FastAPI
from typing import List
from unittest import result
from fastapi import APIRouter, HTTPException, Request, status
from fastapi.params import Body
from fastapi.encoders import jsonable_encoder

# Models
from app.src.models.history import History

router = APIRouter()


# Teachers

@router.post(
    path="/new",
    response_model=History,
    status_code=status.HTTP_201_CREATED,
    tags=["History"]
)
def create_history(request: Request, history: History = Body(...)):
    history = jsonable_encoder(history)
    new_history = request.app.database["history"].insert_one(history)
    created_history = request.app.database["history"].find_one(
        {"_id": new_history.inserted_id})
    return created_history


@router.get(
    path="/",
    response_model=List[History],
    status_code=status.HTTP_200_OK,
    tags=["History"]
)
def get_payments(request: Request):
    results = list(request.app.database["history"].find(limit=100))
    return results
