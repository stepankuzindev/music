from typing import List

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

import app.db.base as models
import app.schemas.author as schemas


def create_author(
    db: Session,
    author: schemas.AuthorIn,
) -> models.Author:
    db_author = models.Author(**author.dict())
    models.save(db=db, object=db_author)

    return db_author


def get_authors(db: Session) -> List[models.Author]:
    authors = db.query(models.Author).all()

    return authors


def get_author(
    db: Session,
    author_id: int,
) -> models.Author:
    author = db.query(models.Author).get(author_id)
    if not author:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Not found Author with id = {author_id}",
        )

    return author


def delete_author(
    db: Session,
    author_id: int,
) -> models.Author:
    author = db.query(models.Author).get(author_id)
    if not author:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Not found Author with id = {author_id}",
        )

    models.delete(db=db, object=author)

    return author
