# FastAPI
from typing import List
from fastapi import APIRouter, Request, status, HTTPException
from fastapi.params import Body
from fastapi.encoders import jsonable_encoder

# logger
from app import logger

# Models
from app.src.models.staff import Teacher, Administrative

router = APIRouter()


@router.post(
    path="/teacher/new",
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
    teacher = jsonable_encoder(teacher)
    new_teacher = request.app.database["teachers"].insert_one(teacher)
    created_teacher = request.app.database["teachers"].find_one(
        {"_id": new_teacher.inserted_id})
    logger.info(f"A new teacher has been added: {teacher.name}")
    return created_teacher


@router.get(
    path="/teacher",
    response_model=List[Teacher],
    status_code=status.HTTP_200_OK,
    tags=["Teachers"]
)
def get_teachers(request: Request):
    """
    It gets a list of teachers from the database

    :param request: Request
    :type request: Request
    :return: A list of teachers
    """
    try:
        logger.info(f"The list of teachers has been requested")
        teachers = list(request.app.database["teachers"].find(limit=100))
        return teachers
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@router.get(
    path="/teacher/{_id}",
    response_model=Teacher,
    status_code=status.HTTP_200_OK,
    tags=["Teachers"]
)
def get_teacher_by_id(request: Request, _id: str):
    """
    If the teacher exists, return it, otherwise raise an exception

    :param request: Request - this is the request object that is passed to the function
    :type request: Request
    :param _id: The ID of the teacher to get
    :type _id: str
    :return: The teacher with the given ID.
    """
    if (teacher := request.app.database["teachers"].find_one({"_id": _id})) is not None:
        return teacher
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Teacher with ID {_id} not found")


@router.post(
    path="/admin/new",
    response_model=Administrative,
    status_code=status.HTTP_201_CREATED,
    tags=["Administrative Staff"]
)
def create_administrative(request: Request, administrative: Administrative = Body(...)):
    """
    It creates a new administrative staff member

    :param request: Request - This is the request object that is passed to the function
    :type request: Request
    :param administrative: Administrative = Body(...)
    :type administrative: Administrative
    :return: The created_staff is being returned.
    """
    staff = jsonable_encoder(administrative)
    new_staff = request.app.database["administrative_staff"].insert_one(staff)
    created_staff = request.app.database["administrative_staff"].find_one(
        {"_id": new_staff.inserted_id})
    logger.info(f"A new staff member has been added: {administrative.name}")
    return created_staff


@router.get(
    path="/admin",
    response_model=List[Administrative],
    status_code=status.HTTP_200_OK,
    tags=["Administrative Staff"]
)
def get_administrative_staff(request: Request):
    """
    `get_administrative_staff` returns a list of the first 100 administrative staff members from the
    database

    :param request: Request
    :type request: Request
    :return: A list of dictionaries.
    """
    logger.info(f"The list of the staff has been requested")
    staff = list(request.app.database["administrative_staff"].find(limit=100))
    return staff


@router.get(
    path="/admin/{_id}",
    response_model=Administrative,
    status_code=status.HTTP_200_OK,
    tags=["Administrative Staff"]
)
def get_administrative_by_id(request: Request, _id: str):
    """
    It takes a request and an ID, and returns the administrative staff member with that ID

    :param request: Request - This is the request object that is passed to the function
    :type request: Request
    :param _id: The ID of the administrative staff member to retrieve
    :type _id: str
    :return: The administrative staff with the given ID.
    """
    if (staff := request.app.database["administrative_staff"].find_one({"_id": _id})) is not None:
        return staff
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Administrative with ID {_id} not found")
