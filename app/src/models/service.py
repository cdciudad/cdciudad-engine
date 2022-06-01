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


class ServiceCard(BaseModel):
    id: UUID = Field(default=uuid4(), alias='_id')

    name: str = Field(..., example="Dunder Mifflin Paper Company")
    description: str = Field(..., example="The company was founded by Robert Dunder and Robert Mifflin in 1949, where they supplied metal brackets. Eventually, the company started selling paper and opened several branches across the Northeastern United States.")
    banner_picture: str = Field(
        ..., example="https://static.wikia.nocookie.net/theoffice/images/2/2d/Dunder_Mifflin%2C_Inc_Long.jpg/revision/latest/scale-to-width-down/350?cb=20180717195405")


class Service(BaseModel):

    id: UUID = Field(default=uuid4(), alias='_id')

    name: str = Field(..., example="Dunder Mifflin Paper Company")
    description: str = Field(..., example="The company was founded by Robert Dunder and Robert Mifflin in 1949, where they supplied metal brackets. Eventually, the company started selling paper and opened several branches across the Northeastern United States.")
    procedure: List[str] = Field(..., example=[
                                 "Come to our offices or contact one of our vendors."])

    contacts: List[ServiceContact] = Field(..., example=[{
        "duty_manager": "Michael Scott",
        "email": "michaelscott@mail.com",
        "phone": "(507) 343-3400",
        "office_hours": "Employees come in long past 9:00 AM and leave before 5:00 PM"}])

    banner_picture: str = Field(
        ..., example="https://static.wikia.nocookie.net/theoffice/images/2/2d/Dunder_Mifflin%2C_Inc_Long.jpg/revision/latest/scale-to-width-down/350?cb=20180717195405")
    gallery: List[str] = Field(..., example=["https://fotografias.antena3.com/clipping/cmsimages01/2017/12/19/EAEC72BC-CAA6-4832-A28B-617A6BA2711C/69.jpg?crop=4:3,smart&width=1200&height=900&optimize=low&format=webply",
                               "https://i.etsystatic.com/8542346/r/il/cffc05/2603525644/il_570xN.2603525644_s6tw.jpg"])

    class Config:
        allow_population_by_field_name = True
