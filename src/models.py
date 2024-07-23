import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from eralchemy2 import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(25),unique=True, nullable=False)
    email = Column(String(25),unique=True, nullable=False)
    password = Column(String(10), nullable=False)
    
class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False)
    gender = Column(String(25), nullable=False)
    eye_color = Column(String(10), nullable=False)
    age = Column(Integer, nullable=False)
    users = relationship(Users)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False)
    terrain = Column(String(50), nullable=False)
    diameter = Column(Integer, nullable=False)
    atmosphere = Column(String(50), nullable=False)
    users = relationship(Users)

class StarShips(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False)
    passengers = Column(Integer, nullable=False)
    manufacturer = Column(String(25), nullable=False)
    users = relationship(Users)

class FavoriteCharacters(Base):
    __tablename__ = 'favoriteCharacters'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    characters_id = Column(Integer, ForeignKey('characters.id'))

class FavoritePlanets(Base):
    __tablename__ = 'favoritePlanets'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    planets_id = Column(Integer, ForeignKey('planets.id'))

class FavoriteStarShips(Base):
    __tablename__ = 'favoriteStarShips'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    starShips_id = Column(Integer, ForeignKey('starships.id'))

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
