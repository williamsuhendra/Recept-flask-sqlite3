import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Recept(Base):
    __tablename__ = 'recept'
    recept_id = Column(Integer,primary_key=True)
    naam = Column(String(20), unique=True, nullable = False)
    hoeveel = Column(String(100))
    foto = Column(String(100))
    typegerecht = Column(String(100))
    bereidingstijd = Column(String(100))
    landvanherkomst = Column(String(100))
    is_vegetarish = Column(Boolean)
    datum = Column(DateTime)
    #ingridienten = relationship('ingridient', backref='nodig')
    #bereidingstappen = relationship('bereidingsstap', backref='volg')
    #apparatuur = relationship('extra', backref='gebruik')


class Ingridient(Base):
    __tablename__ = 'ingridient'
    ingri_id = Column(Integer,primary_key=True)
    hoevelheid = Column(String(10))
    naam = Column(String(40))
    recept_id = Column(Integer, ForeignKey('recept'))
    recept_ingridient = relationship("Recept")


class Bereidingsstap(Base):
    __tablename__ = 'bereidingsstap'
    bereid_id = Column(Integer,primary_key=True)
    teksten = Column(String(200))
    recept_id = Column(Integer, ForeignKey('recept'))
    recept_bereidingsstap = relationship("Recept")

class Extra(Base):
    __tablename__ = 'extra'
    extra_id = Column(Integer,primary_key=True)
    teksten = Column(String(200))
    recept_id = Column(Integer, ForeignKey('recept'))
    recept_extra = relationship("Recept")


# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///sqlalchemy_example.db')

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)