# FastAPI
from typing import List
from fastapi import APIRouter, HTTPException, Request, status
from fastapi.params import Body
from fastapi.encoders import jsonable_encoder

from app import logger

# Models
from app.src.models.payment import Payment

router = APIRouter()


@router.post(
    path="/new",
    response_model=Payment,
    status_code=status.HTTP_201_CREATED,
    tags=["Payments"]
)
def create_payment(request: Request, payment: Payment = Body(...)):
    """
    It creates a new payment method

    :param request: Request - The request object
    :type request: Request
    :param payment: Payment = Body(...)
    :type payment: Payment
    :return: The created payment method.
    """
    payment = jsonable_encoder(payment)
    new_payment = request.app.database["payments"].insert_one(payment)
    created_payment = request.app.database["payments"].find_one(
        {"_id": new_payment.inserted_id})
    logger.info(f"A new payment method has been added: {payment.name}")
    return created_payment


@router.get(
    path="/",
    response_model=List[Payment],
    status_code=status.HTTP_200_OK,
    tags=["Payments"]
)
def get_payments(request: Request):
    """
    It returns a list of payments from the database

    :param request: Request - This is the request object that is passed to the function
    :type request: Request
    :return: A list of payments
    """
    logger.info(f"The list of payment methods has been requested")
    payment = list(request.app.database["payments"].find(limit=100))
    return payment


@router.get(
    path="/{_id}",
    response_model=Payment,
    status_code=status.HTTP_200_OK,
    tags=["Payments"]
)
def get_payment_by_id(request: Request, _id: str):
    """
    If the payment with the given ID exists, return it, otherwise raise an exception

    :param request: Request - this is the request object that is passed to the function
    :type request: Request
    :param _id: The ID of the payment to retrieve
    :type _id: str
    :return: A payment object
    """
    if (payment := request.app.database["payments"].find_one({"_id": _id})) is not None:
        return payment
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Payment with ID {_id} not found")
