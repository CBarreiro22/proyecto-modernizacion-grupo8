from sqlalchemy import Column, Integer, String, ForeignKey
from .declarative_base import Base

class Mantenimiento(Base):
    __tablename__ = 'mantenimiento'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    descripcion = Column(String)




