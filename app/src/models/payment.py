# Python
from typing import List
from typing_extensions import TypedDict
from uuid import UUID, uuid4

# Pydantic
from pydantic.fields import Field
from pydantic import BaseModel


class PaymentStep(TypedDict):
    image: str
    name: str
    description: str
    link: str
    alternative_text: str


class Payment(BaseModel):

    id: UUID = Field(default=uuid4(), alias='_id')

    name: str = Field(...)
    description: str = Field(...)

    video: str = Field(...)
    video_cover: str = Field(...)
    payment_guide: List[PaymentStep] = Field(...)

    class Config:
        allow_population_by_field_name = True
