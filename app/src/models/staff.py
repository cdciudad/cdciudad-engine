# Python
from doctest import Example
from uuid import UUID, uuid4
from typing import List

# Pydantic
from pydantic import BaseModel
from pydantic.fields import Field

# Department
from app.src.models.department import Department


class Staff(BaseModel):

    id: UUID = Field(default=uuid4(), alias='_id')

    name: str = Field(...)
    department: Department = Field(...)
    hello_there: str = Field(...)
    experience: str = Field(...)

    job: str = Field(...)
    hobbies: List[str] = Field(...)
    years_of_experience: int = Field(...)

    banner_picture: str = Field(...)
    profile_picture: str = Field(...)

    class Config:
        allow_population_by_field_name = True
