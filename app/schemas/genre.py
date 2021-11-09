from app.schemas.base import BaseSchema


class GenreIn(BaseSchema):
    name: str


class GenreOut(BaseSchema):
    id: int
    name: str
    tracks: list


class GenreOutShort(BaseSchema):
    id: int
    name: str
