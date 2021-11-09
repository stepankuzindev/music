from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

import app.db.base as models
import app.schemas.tag as schemas
import app.services.tag as services
from app.db.session import get_db

router = APIRouter()


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.TagOut,
)
def create_tag(
    tag: schemas.TagIn,
    db: Session = Depends(get_db),
) -> models.Tag:
    return services.create_tag(db=db, tag=tag)


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=List[schemas.TagOut],
)
def get_tags(db: Session = Depends(get_db)) -> List[models.Tag]:
    return services.get_tags(db=db)


@router.get(
    "/{tag_id}",
    status_code=status.HTTP_200_OK,
    response_model=schemas.TagOut,
)
def get_tag(
    tag_id: int,
    db: Session = Depends(get_db),
) -> models.Tag:
    return services.get_tag(db=db, tag_id=tag_id)


@router.delete(
    "/{tag_id}",
    status_code=status.HTTP_200_OK,
    response_model=schemas.TagOut,
)
def delete_tag(
    tag_id: int,
    db: Session = Depends(get_db),
) -> models.Tag:
    return services.delete_tag(db=db, tag_id=tag_id)
