# FastAPI
from fastapi import APIRouter, status
from fastapi.params import Body

# Models
from app.models.subscriber import Subscriber
from app.services.subscribers import SubscribersService

router = APIRouter()
service = SubscribersService()

# Path Operations


@router.post(
    path="/subscribe",
    response_model=Subscriber,
    status_code=status.HTTP_201_CREATED
)
def subscribe(sub: Subscriber = Body(...)):
    return service.subscribe(sub)
