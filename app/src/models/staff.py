# Python
from typing import List
from uuid import UUID, uuid4
from typing_extensions import TypedDict

# Pydantic
from pydantic.fields import Field
from pydantic.networks import EmailStr
from pydantic import BaseModel

# Models
from app.src.models.department import AdministrativeDepartment, TeachingDepartment


class Staff(BaseModel):

    id: UUID = Field(default=uuid4(), alias='_id')

    name: str = Field(...)
    hello_there: str = Field(...)
    experience: str = Field(...)

    job: str = Field(...)
    hobbies: List[str] = Field(...)
    years_of_experience: int = Field(...)

    banner_picture: str = Field(...)
    profile_picture: str = Field(...)

    class Config:
        allow_population_by_field_name = True


class Teacher(Staff):

    department: TeachingDepartment = Field(...)
    schooling: List[str] = Field(...)
    courses: List[str] = Field(...)


class Contact(TypedDict):
    email: EmailStr
    phone: str
    office_hours: str


class Administrative(Staff):

    department: AdministrativeDepartment = Field(...)
    what_i_do: List[str] = Field(...)
    contact: Contact = Field(...)
