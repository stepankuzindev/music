from app.schemas.author import AuthorOutShort
from app.schemas.base import BaseSchema
from app.schemas.genre import GenreOutShort
from app.schemas.tag import TagOutShort


class TrackIn(BaseSchema):
    name: str
    author_id: int
    genre_id: int
    tag_id: int


class TrackOut(BaseSchema):
    id: int
    name: str

    author_id: int
    author: AuthorOutShort

    genre_id: int
    genre: GenreOutShort

    tag_id: int
    tag: TagOutShort
