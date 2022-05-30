# FastAPI
from fastapi import APIRouter, Request, status
from fastapi.params import Body
from fastapi.encoders import jsonable_encoder

# Python
from typing import List

# Models
from app.src.models.history import HistoryPost, HistoryVideo

router = APIRouter()


@router.post(
    path="/new",
    response_model=HistoryPost,
    status_code=status.HTTP_201_CREATED,
    tags=["History"]
)
def create_history(request: Request, history: HistoryPost = Body(...)):
    """
    ## Create History

    It takes a history object, encodes it to JSON, inserts it into the database, and returns the newly
    created history object

    ### Args:
    - request: Request - The request object
    - history: History - The history posts

    ### Returns: 
    A new history object is being returned.
    """
    history = jsonable_encoder(history)
    new_history = request.app.database["history"].insert_one(history)
    created_history = request.app.database["history"].find_one(
        {"_id": new_history.inserted_id})
    return created_history


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
