from sqlalchemy import *
from sqlalchemy.orm import relationship
from .declarative_base import Base
from datetime import datetime


class Accion(Base):
    __tablename__ = 'accion'
    id = Column(Integer, primary_key=True)
    mantenimiento = Column(Integer, ForeignKey('mantenimiento.id'))
    kilometraje = Column(Integer)
    fecha = Column(DateTime())
    costo = Column(Float)
    automovil = Column(Integer, ForeignKey('automovil.id'))
