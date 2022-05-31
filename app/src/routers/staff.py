# FastAPI
from fastapi import APIRouter, Request, status, HTTPException
from fastapi.params import Body
from fastapi.encoders import jsonable_encoder

# Python
from app import logger
from typing import List

# Models
from app.src.models.staff import Staff, StaffCard

router = APIRouter()


@router.get(
    path="/",
    response_model=List[StaffCard],
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
