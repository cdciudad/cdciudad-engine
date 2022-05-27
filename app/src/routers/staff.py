# FastAPI
from typing import List
from fastapi import APIRouter, Request, status, HTTPException
from fastapi.params import Body
from fastapi.encoders import jsonable_encoder

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
def create_teacher(request: Request, teacher: Teacher = Body(...)):
    teacher = jsonable_encoder(teacher)
    new_teacher = request.app.database["teachers"].insert_one(teacher)
    created_teacher = request.app.database["teachers"].find_one(
        {"_id": new_teacher.inserted_id})
    return created_teacher


@router.get(
    path="/teacher",
    response_model=List[Teacher],
    status_code=status.HTTP_200_OK,
    tags=["Teachers"]
)
def get_teachers(request: Request):
    teachers = list(request.app.database["teachers"].find(limit=100))
    return teachers


@router.get(
    path="/teacher/{_id}",
    response_model=Teacher,
    status_code=status.HTTP_200_OK,
    tags=["Teachers"]
)
def get_teacher_by_id(request: Request, _id: str):
    if (teacher := request.app.database["teachers"].find_one({"_id": _id})) is not None:
        return teacher
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Teacher with ID {_id} not found")


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
