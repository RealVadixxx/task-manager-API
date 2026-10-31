from src.schemas.base import Base


class TaskSchema(Base):
    id: int
    name: str

class TaskCreate(Base):
    name: str

class TaskGet(Base):
    id: int

class TaskRename(Base):
    id: int
    new_name: str

class TaskDelete(Base):
    id: int