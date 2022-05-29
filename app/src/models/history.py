# Python
from typing import List
from uuid import UUID, uuid4

# Pydantic
from pydantic.fields import Field
from pydantic import BaseModel


class History(BaseModel):

    id: UUID = Field(default=uuid4(), alias='_id')

    name: str = Field(...)
    contents: List[str] = Field(...)

    video: str = Field(...)
    video_cover: str = Field(...)
    gallery: List[str] = Field(...)

    class Config:
        allow_population_by_field_name = True
