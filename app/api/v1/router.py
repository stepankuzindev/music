from fastapi import APIRouter

from .endpoints import author, genre, healthcheck, tag, track

api_router = APIRouter()
api_router.include_router(healthcheck.router, prefix="/healthcheck")
api_router.include_router(author.router, prefix="/author", tags=["Author"])
api_router.include_router(genre.router, prefix="/genre", tags=["Genre"])
api_router.include_router(tag.router, prefix="/tag", tags=["Tag"])
api_router.include_router(track.router, prefix="/track", tags=["Track"])
