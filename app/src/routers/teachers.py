# FastAPI
from typing import List
from fastapi import APIRouter, status
from fastapi.params import Body

# Models
from app.src.models.teacher import Teacher

router = APIRouter()


@router.get(
    path="/teacher",
    response_model=List[Teacher],
    status_code=status.HTTP_200_OK,
    tags=["Teachers"]
)
def get_teachers():
    return 'ok'
