from typing import List

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

import app.db.base as models
import app.schemas.track as schemas


def create_track(
    db: Session,
    track: schemas.TrackIn,
) -> models.Track:
    db_track = models.Track(**track.dict())
    models.save(db=db, object=db_track)

    return db_track


def get_tracks(db: Session) -> List[models.Track]:
    tracks = db.query(models.Track).all()

    return tracks


def get_track(
    db: Session,
    track_id: int,
) -> models.Track:
    track = db.query(models.Track).get(track_id)
    if not track:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Not found Track with id = {track_id}",
        )

    return track


def delete_track(
    db: Session,
    track_id: int,
) -> models.Track:
    track = db.query(models.Track).get(track_id)
    if not track:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Not found Track with id = {track_id}",
        )

    models.delete(db=db, object=track)

    return track
