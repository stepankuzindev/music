from typing import List

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

import app.db.base as models
import app.schemas.tag as schemas


def create_tag(
    db: Session,
    tag: schemas.TagIn,
) -> models.Tag:
    db_tag = models.Tag(**tag.dict())
    models.save(db=db, object=db_tag)

    return db_tag


def get_tags(db: Session) -> List[models.Tag]:
    tags = db.query(models.Tag).all()

    return tags


def get_tag(
    db: Session,
    tag_id: int,
) -> models.Tag:
    tag = db.query(models.Tag).get(tag_id)
    if not tag:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Not found Tag with id = {tag_id}",
        )

    return tag


def delete_tag(
    db: Session,
    tag_id: int,
) -> models.Tag:
    tag = db.query(models.Tag).get(tag_id)
    if not tag:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Not found Tag with id = {tag_id}",
        )

    models.delete(db=db, object=tag)

    return tag


def put_tag(
    db: Session,
    tag: schemas.TagIn,
    tag_id: int,
) -> None:
    tag_qs = db.query(models.Tag).filter_by(id=tag_id)
    if not tag_qs:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Not found Tag with id = {tag_id}",
        )

    tag_qs.update(tag.dict())
    models.update(db=db)
