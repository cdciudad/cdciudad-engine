# FastAPI
from typing import List
from fastapi import APIRouter, HTTPException, Request, status
from fastapi.params import Body
from fastapi.encoders import jsonable_encoder

from app import logger

# Models
from app.src.models.subscriber import Subscriber

router = APIRouter()


@router.post(
    path="/new",
    response_model=Subscriber,
    status_code=status.HTTP_201_CREATED,
    tags=["Subscribers"]
)
def subscribe(request: Request, sub: Subscriber = Body(...)):
    """
    If the email address is not already in the database, add it

    :param request: Request - The request object
    :type request: Request
    :param sub: Subscriber = Body(...)
    :type sub: Subscriber
    :return: The created_sub is being returned.
    """
    if (s := request.app.database["subscribers"].find_one({"email": sub.email})) is None:
        subscriber = jsonable_encoder(sub)
        new_sub = request.app.database["subscribers"].insert_one(subscriber)
        created_sub = request.app.database["subscribers"].find_one(
            {"_id": new_sub.inserted_id})
        logger.info(f"A new subscriber has been added: {sub.email}")
        return created_sub

    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail=f"Email {subscriber.email} is already subscribed")


@router.get(path="/", response_model=List[Subscriber], tags=["Subscribers"])
def get_subscribers(request: Request):
    """
    It gets the first 100 subscribers from the database

    :param request: Request
    :type request: Request
    :return: A list of dictionaries.
    """
    subs = list(request.app.database["subscribers"].find(limit=100))
    return subs
