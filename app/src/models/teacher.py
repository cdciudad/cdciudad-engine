# Python
from typing import List

# Pydantic
from pydantic.fields import Field

# Staff
from app.src.models.staff import Staff
from app.src.models.department import TeachingDepartment


class Teacher(Staff):

    department: TeachingDepartment = Field(...)
    schooling: List[str] = Field(...)
    courses: List[str] = Field(...)
