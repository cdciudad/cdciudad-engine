# Python
from datetime import datetime
from uuid import UUID, uuid4

# Pydantic
from pydantic import BaseModel
from pydantic.fields import Field
from pydantic.networks import EmailStr


class Subscriber(BaseModel):

    sub_id: UUID = Field(default=uuid4())
    email: EmailStr = Field(...)
    created_at: datetime = Field(default=datetime.now())
