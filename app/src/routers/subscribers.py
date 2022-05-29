# FastAPI
from typing import List
from fastapi import APIRouter, HTTPException, Request, status
from fastapi.params import Body
from fastapi.encoders import jsonable_encoder

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
    if (s := request.app.database["subscribers"].find_one({"email": sub.email})) is None:
        subscriber = jsonable_encoder(sub)
        new_sub = request.app.database["subscribers"].insert_one(subscriber)
        created_sub = request.app.database["subscribers"].find_one(
            {"_id": new_sub.inserted_id})
        return created_sub

    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail=f"Email {subscriber.email} is already subscribed")


@router.get(path="/", response_model=List[Subscriber], tags=["Subscribers"])
def get_subscribers(request: Request):
    subs = list(request.app.database["subscribers"].find(limit=100))
    return subs
