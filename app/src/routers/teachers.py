# FastAPI
from fastapi import APIRouter, Request, status, HTTPException
from fastapi.params import Body
from fastapi.encoders import jsonable_encoder

# Python
from app import logger
from typing import List
import random

# Models
from app.src.models.staff import StaffCard, Teacher

router = APIRouter()


@router.get(
    path="/",
    response_model=List[StaffCard],
    status_code=status.HTTP_200_OK,
    tags=["Teachers"]
)
def get_teachers(request: Request):
    """
    ## Get teacher

    It gets a list of teachers from the database

    ## Args:
    - request: Request

    ## Returns: 
    A list of teachers
    """
    try:
        logger.info(f"The list of teachers has been requested")
        teachers = list(request.app.database["teachers"].find(limit=100))
        return teachers
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@router.get(
    path="/random",
    response_model=List[StaffCard],
    status_code=status.HTTP_200_OK,
    tags=["Teachers"]
)
def get_random_teachers(request: Request):
    try:
        logger.info(f"The list of 5 random teachers has been requested")
        teachers = list(request.app.database["teachers"].find())
        return random.sample(teachers, k=5)
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@router.get(
    path="/{_id}",
    response_model=Teacher,
    status_code=status.HTTP_200_OK,
    tags=["Teachers"]
)
def get_teacher_by_id(request: Request, _id: str):
    """
    ## Get teacher by ID

    If the teacher exists, return it, otherwise raise an exception

    ## Args:
    - request: Request - this is the request object that is passed to the function
    - _id: The ID of the teacher to get

    ## Returns:
    The teacher with the given ID.
    """
    if (teacher := request.app.database["teachers"].find_one({"_id": _id})) is not None:
        return teacher
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Teacher with ID {_id} not found")
