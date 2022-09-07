from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .declarative_base import Base


class Mantenimiento(Base):
    __tablename__ = 'mantenimiento'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    descripcion = Column(String)
    acciones = relationship('Accion', cascade='all, delete, delete-orphan')


