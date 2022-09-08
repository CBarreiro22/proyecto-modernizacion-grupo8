from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .declarative_base import Base
from src.modelo.accion import Accion 

class Auto(Base):
    __tablename__ = 'auto'
    id = Column(Integer, primary_key=True)
    marca = Column(String)
    placa = Column(String)
    modelo = Column(Integer)
    kilometraje = Column(Integer)
    color = Column(String)
    cilindraje = Column(Integer)
    combustible = Column(String)
    acciones = relationship('Accion', cascade='all, delete, delete-orphan')