from typing import List

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

import app.db.base as models
import app.schemas.genre as schemas


def create_genre(
    db: Session,
    genre: schemas.GenreIn,
) -> models.Genre:
    db_genre = models.Genre(**genre.dict())
    models.save(db=db, object=db_genre)

    return db_genre


def get_genres(db: Session) -> List[models.Genre]:
    genres = db.query(models.Genre).all()

    return genres


def get_genre(
    db: Session,
    genre_id: int,
) -> models.Genre:
    genre = db.query(models.Genre).get(genre_id)
    if not genre:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Not found Genre with id = {genre_id}",
        )

    return genre


def delete_genre(
    db: Session,
    genre_id: int,
) -> models.Genre:
    genre = db.query(models.Genre).get(genre_id)
    if not genre:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Not found Genre with id = {genre_id}",
        )

    models.delete(db=db, object=genre)

    return genre
