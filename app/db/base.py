# Import all the models, so that Base has them before being
# imported by Alembic
from typing import Any

from sqlalchemy import exc

from app.db.base_class import Base  # noqa
from app.models.models import Author, Genre, Tag, Track  # noqa


def save(db: Any, data: Any) -> None:
    try:
        db.add(data)
        db.commit()
        db.refresh(data)
    except exc.SQLAlchemyError as e:
        raise e
