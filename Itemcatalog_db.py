import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))

class MovieType(Base):
    __tablename__ = 'movietype'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
        }


class MoviePage(Base):
    __tablename__ = 'moviepage'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    Storyline = Column(String(250))
    link = Column(String(250))
    Director = Column(String(80))
    stars = Column(String(250))
    release = Column(String(250))
    movietype_id = Column(Integer, ForeignKey('movietype.id'))
    movietype = relationship(MovieType)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'Storyline': self.Storyline,
            'link': self.link,
            'Director': self.Director,
            'stars': self.stars,
            'release': self.release,
            'id': self.id,

        }


engine = create_engine('sqlite:///Movie_page.db')


Base.metadata.create_all(engine)
