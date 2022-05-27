# FastAPI
from typing import List
from fastapi import APIRouter, status
from fastapi.params import Body

# Models
from app.src.models.staff import Teacher, Administrative

router = APIRouter()

# Teachers


@router.post(
    path="/teacher/new",
    response_model=Teacher,
    status_code=status.HTTP_201_CREATED,
    tags=["Teachers"]
)
def create_teacher(teacher: Teacher = Body(...)):
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
    path="/teacher/{_id}",
    response_model=Teacher,
    status_code=status.HTTP_200_OK,
    tags=["Teachers"]
)
def get_teacher_by_id(_id: str):
    return 'ok'


# Administrative Staff
@router.post(
    path="/admin/new",
    response_model=Administrative,
    status_code=status.HTTP_201_CREATED,
    tags=["Administrative Staff"]
)
def create_administrative(administrative: Administrative = Body(...)):
    return administrative


@router.get(
    path="/admin",
    response_model=List[Administrative],
    status_code=status.HTTP_200_OK,
    tags=["Administrative Staff"]
)
def get_administrative_staff():
    return 'ok'


@router.get(
    path="/admin/{_id}",
    response_model=Administrative,
    status_code=status.HTTP_200_OK,
    tags=["Administrative Staff"]
)
def get_administrative_by_id(_id: str):
    return 'ok'
