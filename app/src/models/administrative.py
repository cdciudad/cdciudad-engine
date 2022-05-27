# Python
from typing import List, TypedDict

# Pydantic
from pydantic.fields import Field
from pydantic.networks import EmailStr

# Models
from app.src.models.staff import Staff
from app.src.models.department import AdministrativeDepartment


class Contact(TypedDict):
    email: EmailStr
    phone: str
    office_hours: str


class Administrative(Staff):

    department: Department = Field(...)
    what_i_do: List[str] = Field(...)
    contact: Contact = Field(...)
