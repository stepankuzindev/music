from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

import app.db.base as models
import app.schemas.track as schemas
import app.services.track as services
from app.db.session import get_db

router = APIRouter()


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.TrackOut,
)
def create_track(
    track: schemas.TrackIn,
    db: Session = Depends(get_db),
) -> models.Track:
    return services.create_track(db=db, track=track)


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=List[schemas.TrackOut],
)
def get_tracks(db: Session = Depends(get_db)) -> List[models.Track]:
    return services.get_tracks(db=db)


@router.get(
    "/{track_id}",
    status_code=status.HTTP_200_OK,
    response_model=schemas.TrackOut,
)
def get_track(
    track_id: int,
    db: Session = Depends(get_db),
) -> models.Track:
    return services.get_track(db=db, track_id=track_id)


@router.delete(
    "/{track_id}",
    status_code=status.HTTP_200_OK,
    response_model=schemas.TrackOut,
)
def delete_track(
    track_id: int,
    db: Session = Depends(get_db),
) -> models.Track:
    return services.delete_track(db=db, track_id=track_id)


@router.put(
    "/{track_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def put_track(
    track_id: int,
    track: schemas.TrackIn,
    db: Session = Depends(get_db),
) -> None:
    services.put_track(db=db, track=track, track_id=track_id)
