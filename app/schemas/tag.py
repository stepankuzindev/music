from app.schemas.base import BaseSchema


class TagIn(BaseSchema):
    name: str


class TagOut(BaseSchema):
    id: int
    name: str
    tracks: list


class TagOutShort(BaseSchema):
    id: int
    name: str
