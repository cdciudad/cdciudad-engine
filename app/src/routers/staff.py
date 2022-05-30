# FastAPI
from fastapi import APIRouter, Request, status, HTTPException
from fastapi.params import Body
from fastapi.encoders import jsonable_encoder

# Python
from app import logger
from typing import List

# Models
from app.src.models.staff import Staff

router = APIRouter()


@router.post(
    path="/new",
    response_model=Staff,
    status_code=status.HTTP_201_CREATED,
    tags=["Staff"]
)
def create_staff(request: Request, administrative: Staff = Body(...)):
    """
    ## Create Staff

    It creates a new staff member.

    ### Args:
    - request: Request - This is the request object that is passed to the function.
    - staff: Staff = Body(...)

    ### Returns: 
    The created_staff is being returned.
    """
    staff = jsonable_encoder(administrative)
    new_staff = request.app.database["staff"].insert_one(staff)
    created_staff = request.app.database["staff"].find_one(
        {"_id": new_staff.inserted_id})
    logger.info(f"A new staff member has been added: {administrative.name}")
    return created_staff


@router.get(
    path="/",
    response_model=List[Staff],
    status_code=status.HTTP_200_OK,
    tags=["Staff"]
)
def get_staff(request: Request):
    """
    ## Get staff

    Returns a list of the first 100 administrative staff members from the
    database.

    ### Args:
    - request: Request

    ### Returns:  
    A list of dictionaries.
    """
    logger.info(f"The list of the staff has been requested")
    staff = list(request.app.database["staff"].find(limit=100))
    return staff


@router.get(
    path="/{_id}",
    response_model=Staff,
    status_code=status.HTTP_200_OK,
    tags=["Staff"]
)
def get_staff_by_id(request: Request, _id: str):
    """
    ## Get staff by ID

    It takes a request and an ID, and returns the administrative staff member with that ID.

     ### Args:
    - request: Request - This is the request object that is passed to the function.
    - _id: The ID of the administrative staff member to retrieve.

    ### Returns: 
    The administrative staff with the given ID.
    """
    if (staff := request.app.database["staff"].find_one({"_id": _id})) is not None:
        return staff
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Administrative with ID {_id} not found")
