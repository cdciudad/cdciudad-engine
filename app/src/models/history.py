# Python
from typing import List
from uuid import UUID, uuid4

# Pydantic
from pydantic.fields import Field
from pydantic import BaseModel


class HistoryVideo(BaseModel):
    id: UUID = Field(default=uuid4(), alias='_id')
    video: str = Field(...,
                       example="https://www.movingyourlife.com/the-office/")
    thumbnail: str = Field(..., example="https://roost.nbcuni.com/bin/viewasset.html/content/dam/Peacock/Campaign/landingpages/library/theoffice/mainpage/office-social-min.png/_jcr_content/renditions/original")


class HistoryPost(BaseModel):

    id: UUID = Field(default=uuid4(), alias='_id')

    title: str = Field(..., example="The Office")
    content: List[str] = Field(..., example=["The Office is an American mockumentary sitcom television series that depicts the everyday work lives of office employees in the Scranton, Pennsylvania branch of the fictional Dunder Mifflin Paper Company. It aired on NBC from March 24, 2005, to May 16, 2013, spanning a total of nine seasons."])

    gallery: List[str] = Field(..., example=["https://www.alohacriticon.com/wp-content/uploads/2020/02/the-office-tv-serie-sinopsis.jpg",
                               "https://www.fiebreseries.com/wp-content/uploads/2021/04/The-Office_poster_serie0-1-332x381.jpg", "https://www.abc.es/media/series/000/001/848/the-office-2.jpg"])

    class Config:
        allow_population_by_field_name = True
