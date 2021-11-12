from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

import app.db.base as models
import app.schemas.genre as schemas
import app.services.genre as services
from app.db.session import get_db

router = APIRouter()


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.GenreOut,
)
def create_genre(
    genre: schemas.GenreIn,
    db: Session = Depends(get_db),
) -> models.Genre:
    return services.create_genre(db=db, genre=genre)


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=List[schemas.GenreOut],
)
def get_genres(db: Session = Depends(get_db)) -> List[models.Genre]:
    return services.get_genres(db=db)


@router.get(
    "/{genre_id}",
    status_code=status.HTTP_200_OK,
    response_model=schemas.GenreOut,
)
def get_genre(
    genre_id: int,
    db: Session = Depends(get_db),
) -> models.Genre:
    return services.get_genre(db=db, genre_id=genre_id)


@router.delete(
    "/{genre_id}",
    status_code=status.HTTP_200_OK,
    response_model=schemas.GenreOut,
)
def delete_genre(
    genre_id: int,
    db: Session = Depends(get_db),
) -> models.Genre:
    return services.delete_genre(db=db, genre_id=genre_id)


@router.put(
    "/{genre_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def put_author(
    genre_id: int,
    genre: schemas.GenreIn,
    db: Session = Depends(get_db),
) -> None:
    services.put_genre(db=db, genre=genre, genre_id=genre_id)
