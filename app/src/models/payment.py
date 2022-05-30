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

    name: str = Field(..., example="Banco Nacional")
    description: str = Field(..., example="Podés realizar los pagos en línea desde las plataformas del Banco Nacional, Banco Costa Rica, BAC y desde el sitio oficial de FundaTEC.")
    image: str = Field(...,
                       example="https://iconape.com/wp-content/files/oq/208947/svg/208947.svg")

    video: str = Field(...,
                       example="https://www.youtube.com/watch?v=J-zIxD8qHtQ")
    thumbnail: str = Field(...,
                           example="https://i3.ytimg.com/vi/J-zIxD8qHtQ/maxresdefault.jpg")
    payment_guide: List[PaymentStep] = Field(..., example=[{
        "image": "",
        "name": "Paso 1",
        "description": "Ingresá a la dirección web <www.https://www.bncr.fi.cr/>",
        "link": "www.https://www.bncr.fi.cr/",
        "alternative_text": "www.https://www.bncr.fi.cr/"
    }])

    class Config:
        allow_population_by_field_name = True
