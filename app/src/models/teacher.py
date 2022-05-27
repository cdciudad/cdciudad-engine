# Python
from typing import List

# Pydantic
from pydantic.fields import Field

# Staff
from app.src.models.staff import Staff


class Teacher(Staff):

    schooling: List[str] = Field(...)
    courses: List[str] = Field(...)
