from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.settings.settings import settings

engine = create_engine(settings.POSTGRES_URL, pool_pre_ping=True)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
