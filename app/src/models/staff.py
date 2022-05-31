# Python
from typing import List, Optional
from uuid import UUID, uuid4
from typing_extensions import TypedDict

# Pydantic
from pydantic.fields import Field
from pydantic.networks import EmailStr
from pydantic import BaseModel

# Models
from app.src.models.department import AdministrativeDepartment, TeachingDepartment


class StaffBase(BaseModel):

    id: UUID = Field(default=uuid4(), alias='_id')

    name: str = Field(..., example="Michael Scott")
    hello_there: str = Field(..., example="That's what she said!")
    experience: str = Field(...,
                            example="12 years as manager at Dunder Mifflin Paper Company, Scranton.")

    job: str = Field(..., example="Director of Paper Distribution")
    hobbies: List[str] = Field(..., example=["Film director", "Parkour"])
    years_of_experience: int = Field(..., example=20)

    banner_picture: str = Field(
        ..., example="https://static.wikia.nocookie.net/theoffice/images/7/75/YoungMichaelScott.jpg/revision/latest/scale-to-width-down/180?cb=20200413232331")
    profile_picture: str = Field(
        ..., example="https://pbs.twimg.com/profile_images/1818543591/ms_main_left_400x400.jpg")

    class Config:
        allow_population_by_field_name = True


class Teacher(StaffBase):

    department: TeachingDepartment = Field(
        ..., example=TeachingDepartment.visual_arts_department)
    schooling: List[str] = Field(..., example=[
                                 "University of Scranton's Kania School of Management"])
    courses: List[str] = Field(..., example=["Sales 101"])
    gallery: List[str] = Field(..., example=["https://static.wikia.nocookie.net/theoffice/images/7/75/YoungMichaelScott.jpg/revision/latest/scale-to-width-down/680?cb=20200413232331",
                               "https://static.wikia.nocookie.net/theoffice/images/7/7d/MichaelScottPaperCompany.jpg/revision/latest/top-crop/width/360/height/360?cb=20091216005626"])


class Contact(TypedDict):
    email: EmailStr
    phone: str
    office_hours: str


class Staff(StaffBase):

    department: AdministrativeDepartment = Field(
        ..., example=AdministrativeDepartment.coordination_department)
    what_i_do: List[str] = Field(..., example=[
                                 "Co-Regional Manager", "Regional Manager", "Salesman"])
    contact: Optional[Contact] = Field(
        example={
            "email": "michaelscott@mail.com",
            "phone": "(507) 343-3400",
            "office_hours": "Employees come in long past 9:00 AM and leave before 5:00 PM"})
