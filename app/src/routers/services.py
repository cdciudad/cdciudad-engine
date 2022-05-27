# FastAPI
from typing import List
from fastapi import APIRouter, HTTPException, Request, status
from fastapi.params import Body
from fastapi.encoders import jsonable_encoder

# Models
from app.src.models.service import Service

router = APIRouter()


# Teachers

@router.post(
    path="/new",
    response_model=Service,
    status_code=status.HTTP_201_CREATED,
    tags=["Services"]
)
def create_service(request: Request, service: Service = Body(...)):
    service = jsonable_encoder(service)
    new_service = request.app.database["services"].insert_one(service)
    created_service = request.app.database["services"].find_one(
        {"_id": new_service.inserted_id})
    return created_service


@router.get(
    path="/",
    response_model=List[Service],
    status_code=status.HTTP_200_OK,
    tags=["Services"]
)
def get_services(request: Request):
    services = list(request.app.database["services"].find(limit=100))
    return services


@router.get(
    path="/{_id}",
    response_model=Service,
    status_code=status.HTTP_200_OK,
    tags=["Services"]
)
def get_service_by_id(request: Request, _id: str):
    if (service := request.app.database["services"].find_one({"_id": _id})) is not None:
        return service
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Service with ID {_id} not found")
