from schemas.base import Base


class TaskSchema(Base):
    id: int | None = None
    name: str