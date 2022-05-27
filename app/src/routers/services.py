# FastAPI
from typing import List
from fastapi import APIRouter, status
from fastapi.params import Body

# Models
from app.src.models.service import Service

router = APIRouter()


# Teachers

@router.post(
    path="/new",
    response_model=Service,
    status_code=status.HTTP_201_CREATED,
    tags=["Services"]
)
def create_service(service: Service = Body(...)):
    return service


@router.get(
    path="/",
    response_model=List[Service],
    status_code=status.HTTP_200_OK,
    tags=["Services"]
)
def get_services():
    return 'ok'


@router.get(
    path="/{_id}",
    response_model=Service,
    status_code=status.HTTP_200_OK,
    tags=["Services"]
)
def get_service_by_id(_id: str):
    return 'ok'
