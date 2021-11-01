from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Author(Base):
    __tablename__ = "author"

    id = Column(Integer, primary_key=True)
    name = Column(String)


class Genre(Base):
    __tablename__ = "genre"

    id = Column(Integer, primary_key=True)
    name = Column(String)


class Tag(Base):
    __tablename__ = "tag"

    id = Column(Integer, primary_key=True)
    name = Column(String)


class Track(Base):
    __tablename__ = "track"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    author_id = Column(Integer, ForeignKey("author.id"))
    author = relationship("Author", back_populates="track")

    genre_id = Column(Integer, ForeignKey("genre.id"))
    genre = relationship("Genre", back_populates="track")

    tag_id = Column(Integer, ForeignKey("tag.id"))
    tag = relationship("Tag", back_populates="track")
