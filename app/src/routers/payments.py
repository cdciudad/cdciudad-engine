# FastAPI
from typing import List
from fastapi import APIRouter, HTTPException, Request, status
from fastapi.params import Body
from fastapi.encoders import jsonable_encoder

# Models
from app.src.models.payment import Payment

router = APIRouter()


# Teachers

@router.post(
    path="/new",
    response_model=Payment,
    status_code=status.HTTP_201_CREATED,
    tags=["Payments"]
)
def create_payment(request: Request, payment: Payment = Body(...)):
    payment = jsonable_encoder(payment)
    new_payment = request.app.database["payments"].insert_one(payment)
    created_payment = request.app.database["payments"].find_one(
        {"_id": new_payment.inserted_id})
    return created_payment


@router.get(
    path="/",
    response_model=List[Payment],
    status_code=status.HTTP_200_OK,
    tags=["Payments"]
)
def get_payments(request: Request):
    payment = list(request.app.database["payments"].find(limit=100))
    return payment


@router.get(
    path="/{_id}",
    response_model=Payment,
    status_code=status.HTTP_200_OK,
    tags=["Payments"]
)
def get_payment_by_id(request: Request, _id: str):
    if (payment := request.app.database["payments"].find_one({"_id": _id})) is not None:
        return payment
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Payment with ID {_id} not found")
