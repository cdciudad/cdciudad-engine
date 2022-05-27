# Python
from typing import List
from uuid import UUID, uuid4

# Pydantic
from pydantic.fields import Field
from pydantic import BaseModel

# Models
from app.src.models.staff import Contact


class ServiceContact(Contact):
    duty_manager: str


class Service(BaseModel):

    id: UUID = Field(default=uuid4(), alias='_id')

    name: str = Field(...)
    description: str = Field(...)
    procedure: List[str] = Field(...)

    contacts: List[ServiceContact] = Field(...)

    banner_picture: str = Field(...)
    gallery: List[str] = Field(...)

    class Config:
        allow_population_by_field_name = True
