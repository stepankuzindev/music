from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

import app.db.base as models
import app.schemas.author as schemas
import app.services.author as services
from app.db.session import get_db

router = APIRouter()


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.AuthorOut,
)
def create_author(
    author: schemas.AuthorIn,
    db: Session = Depends(get_db),
) -> models.Author:
    return services.create_author(db=db, author=author)


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=List[schemas.AuthorOut],
)
def get_authors(db: Session = Depends(get_db)) -> List[models.Author]:
    return services.get_authors(db=db)


@router.get(
    "/{author_id}",
    status_code=status.HTTP_200_OK,
    response_model=schemas.AuthorOut,
)
def get_author(
    author_id: int,
    db: Session = Depends(get_db),
) -> models.Author:
    return services.get_author(db=db, author_id=author_id)


@router.delete(
    "/{author_id}",
    status_code=status.HTTP_200_OK,
    response_model=schemas.AuthorOut,
)
def delete_author(
    author_id: int,
    db: Session = Depends(get_db),
) -> models.Author:
    return services.delete_author(db=db, author_id=author_id)
