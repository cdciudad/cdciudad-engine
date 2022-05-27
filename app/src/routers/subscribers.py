# FastAPI
from fastapi import APIRouter, status
from fastapi.params import Body

# Models
from app.src.models.subscriber import Subscriber
from app.src.services.subscribers import SubscribersService

router = APIRouter()
service = SubscribersService()

# Path Operations


@router.post(
    path="/new",
    response_model=Subscriber,
    status_code=status.HTTP_201_CREATED,
    tags=["Subscribers"]
)
def subscribe(sub: Subscriber = Body(...)):
    return service.subscribe(sub)


@router.get(path="/", tags=["Subscribers"])
def get_subscribers():
    return service.get_weekly_subscribers()
