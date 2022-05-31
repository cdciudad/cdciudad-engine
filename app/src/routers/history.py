# FastAPI
from fastapi import APIRouter, Request, status
from fastapi.params import Body
from fastapi.encoders import jsonable_encoder

# Python
from typing import List

# Models
from app.src.models.history import HistoryPost, HistoryVideo

router = APIRouter()


@router.get(
    path="/",
    response_model=List[HistoryPost],
    status_code=status.HTTP_200_OK,
    tags=["History"]
)
def get_history(request: Request):
    """
    ## Get history

    It gets the last 10 entries from the history collection in the database

    ### Args:
    - request: Request

    ### Returns: 
    A list of the last 10 entries in the history posts collection.
    """
    results = list(request.app.database["history"].find(limit=10))
    return results


@router.get(
    path="/video",
    response_model=List[HistoryVideo],
    status_code=status.HTTP_200_OK,
    tags=["History"]
)
def get_history_video(request: Request):
    """
    ## Get history video

    It gets the history videos collection in the database

    ### Args:
    - request: Request

    ### Returns: 
    A list of the last 10 entries in the history videos collection.
    """
    results = list(request.app.database["history-videos"].find(limit=10))
    return results
