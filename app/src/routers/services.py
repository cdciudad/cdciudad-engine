# FastAPI
from fastapi import APIRouter, HTTPException, Request, status
from fastapi.params import Body
from fastapi.encoders import jsonable_encoder

# Python
from app import logger
from typing import List

# Models
from app.src.models.service import Service

router = APIRouter()


@router.post(
    path="/new",
    response_model=Service,
    status_code=status.HTTP_201_CREATED,
    tags=["Services"]
)
def create_service(request: Request, service: Service = Body(...)):
    """
    ## Create service

    It creates a new service

    ## Args:
    - request: Request - This is the request object that is passed to the function
    - service: Service

    ## Returns: 
    The created service.
    """
    service = jsonable_encoder(service)
    new_service = request.app.database["services"].insert_one(service)
    created_service = request.app.database["services"].find_one(
        {"_id": new_service.inserted_id})
    logger.info(f"A new service has been added: {service.name}")
    return created_service


@router.get(
    path="/",
    response_model=List[Service],
    status_code=status.HTTP_200_OK,
    tags=["Services"]
)
def get_services(request: Request):
    """
    ## Get services

    It gets a list of services from the database

    ## Args:
    - request: Request

    ## Returns: 
    A list of services
    """
    logger.info(f"The list of services has been requested")
    services = list(request.app.database["services"].find(limit=100))
    return services


@router.get(
    path="/{_id}",
    response_model=Service,
    status_code=status.HTTP_200_OK,
    tags=["Services"]
)
def get_service_by_id(request: Request, _id: str):
    """
    ## Get service by ID

    If the service exists, return it, otherwise raise an exception

    ## Args:
    - request: Request - The request object that was sent to the endpoint
    - _id: The ID of the service to retrieve

    ## Returns: 
    A service object
    """
    if (service := request.app.database["services"].find_one({"_id": _id})) is not None:
        return service
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Service with ID {_id} not found")
