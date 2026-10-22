from schemas.base import Base


class UserSchema(Base):
    id: int | None = None
    name: str