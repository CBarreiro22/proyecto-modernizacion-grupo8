from sqlalchemy import *
from sqlalchemy.orm import relationship
from .declarative_base import Base
from src.modelo.accion import Accion 

class Automovil(Base):
    __tablename__ = 'automovil'
    id = Column(Integer, primary_key=True)
    marca = Column(String)
    placa = Column(String)
    modelo = Column(Integer)
    kilometraje = Column(Integer)
    color = Column(String)
    cilindraje = Column(Integer)
    combustible = Column(String)
    vendido = Column(Boolean)
    valorVenta = Column(REAL)
    kilometrajeVenta = Column(Integer)
    acciones = relationship('Accion', cascade='all, delete, delete-orphan')