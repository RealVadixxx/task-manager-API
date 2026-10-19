from pydantic import Field
from schemas.base import Base


class TaskSchema(Base):
    name: str = Field(min_length=2, max_length=200)