# FastAPI
from typing import List
from fastapi import APIRouter, status
from fastapi.params import Body

# Models
from app.src.models.teacher import Teacher

router = APIRouter()


@router.post(
    path="/teacher/new",
    response_model=Teacher,
    status_code=status.HTTP_201_CREATED,
    tags=["Teachers"],
    summary="Create Teacher"
)
def create_person(teacher: Teacher = Body(...)):
    return teacher


@router.get(
    path="/teacher",
    response_model=List[Teacher],
    status_code=status.HTTP_200_OK,
    tags=["Teachers"]
)
def get_teachers():
    return 'ok'


@router.get(
    path="/teacher/{teacher_id}",
    response_model=Teacher,
    status_code=status.HTTP_200_OK,
    tags=["Teachers"]
)
def get_teacher_by_id(teacher_id: str):
    return 'ok'
