# Python
from typing import List, TypedDict

# Pydantic
from pydantic.fields import Field
from pydantic.networks import EmailStr

# Staff
from app.src.models.staff import Staff


class Contact(TypedDict):
    email: EmailStr
    phone: str
    office_hours: str


class Administrative(Staff):

    what_i_do: List[str] = Field(...)
    contact: Contact = Field(...)
