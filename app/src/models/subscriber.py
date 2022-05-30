# Python
from uuid import UUID, uuid4
from datetime import datetime

# Pydantic
from pydantic import BaseModel
from pydantic.fields import Field
from pydantic.networks import EmailStr


class Subscriber(BaseModel):
    id: UUID = Field(default=uuid4(), alias='_id')
    email: EmailStr = Field(..., example="michaelscott@mail.com")
    created_at: datetime = Field(default=datetime.now())
