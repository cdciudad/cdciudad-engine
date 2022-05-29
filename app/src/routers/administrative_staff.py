# FastAPI
from typing import List
from fastapi import APIRouter, status
from fastapi.params import Body

# Models
from app.src.models.administrative import Administrative

router = APIRouter()


@router.post(
    path="/administrative/new",
    response_model=Administrative,
    status_code=status.HTTP_201_CREATED,
    tags=["Administrative Staff"]
)
def create_administrative(administrative: Administrative = Body(...)):
    return administrative


@router.get(
    path="/administrative",
    response_model=List[Administrative],
    status_code=status.HTTP_200_OK,
    tags=["Administrative Staff"]
)
def get_administrative_staff():
    return 'ok'


@router.get(
    path="/administrative/{administrative_id}",
    response_model=Administrative,
    status_code=status.HTTP_200_OK,
    tags=["Administrative Staff"]
)
def get_administrative_by_id(administrative_id: str):
    return 'ok'
