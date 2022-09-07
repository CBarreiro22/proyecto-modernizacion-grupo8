from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .declarative_base import Base

class Automovil(Base):
    __tablename__ = 'automovil'
    id = Column(Integer, primary_key=True)
    marca = Column(String)
    placa = Column(String)
    Modelo = Column(Integer)
    kilometraje = Column(Integer)
    color = Column(String)
    cilindraje = Column(Integer)
    combutible = Column(String)
    #acciones = relationship('Accion', cascade='all, delete, delete-orphan')


