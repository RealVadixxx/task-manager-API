from pydantic import Field
from schemas.base import Base


class UserSchema(Base):
    name: str = Field(min_length=2, max_length=40)