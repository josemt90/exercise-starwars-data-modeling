import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er


Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    password = Column(Integer, nullable=False)
    


    

class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    gender = Column(String(100), nullable=False)
    hair_color = Column(String(100), nullable=False)
    height = Column(Integer, nullable=False)
    homeworld = Column(Integer, ForeignKey('planets.id'))
    mass = Column(Integer, nullable=False)
    skin_color = Column(String(100), nullable=False)

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    climate = Column(String(200), nullable=False)
    diameter = Column(Integer, nullable=False)
    gravity = Column(Integer, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    population = Column(Integer, nullable=False)
    terrain = Column(String(200), nullable=False)

class Characters_favourites(Base):
    __tablename__ = 'characters_favourites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    id_character = Column(Integer, ForeignKey('characters.id'))
    characters = relationship(Characters)
    id_user = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Planets_favourites(Base):
    __tablename__ = 'planets_favourites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    id_planets = Column(Integer, ForeignKey('planets.id'))
    planets = relationship(Planets)
    id_user = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')