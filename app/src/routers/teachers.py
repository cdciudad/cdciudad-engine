# FastAPI
from fastapi import APIRouter, Request, status, HTTPException
from fastapi.params import Body
from fastapi.encoders import jsonable_encoder

# Python
from app import logger
from typing import List

# Models
from app.src.models.staff import Teacher

router = APIRouter()


@router.post(
    path="/new",
    response_model=Teacher,
    status_code=status.HTTP_201_CREATED,
    tags=["Teachers"]
)
def create_teacher(request: Request, teacher: Teacher = Body(...)):
    """
    ## Create Teacher

    It creates a new teacher

    ### Args:
    - request: Request - This is the request object that is passed to the function
    - teacher: Teacher - A teacher model with name, greetings, personal information, experience and courses

    ### Returns: 
    The created teacher
    """
    try:
        teacher = jsonable_encoder(teacher)
        new_teacher = request.app.database["teachers"].insert_one(teacher)
        created_teacher = request.app.database["teachers"].find_one(
            {"_id": new_teacher.inserted_id})
    except Exception as e:
        logger.error(f"Error {e}")

    logger.info(f"A new teacher has been added: {teacher['name']}")
    return created_teacher


@router.get(
    path="/",
    response_model=List[Teacher],
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
