from app.schemas.base import BaseSchema


class AuthorIn(BaseSchema):
    name: str


class AuthorOut(BaseSchema):
    id: int
    name: str
    tracks: list


class AuthorOutShort(BaseSchema):
    id: int
    name: str
