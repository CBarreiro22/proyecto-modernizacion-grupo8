from marshmallow import fields, Schema
from sqlalchemy import Column, String, Text, Integer, Boolean, REAL, DateTime, func

from .model import Model


class newCarJsonSchema(Schema):
    id = fields.String()


class Car(Model):
    __tablename__ = 'car'

    brand = Column(String, doc="marca del automovil")
    license_plate = Column(String, doc="placa del vehiculo")
    model = Column(Integer)
    kilometers = Column(Integer)
    color = Column(String)
    displacement = Column(Integer)
    fuel = Column(String)
    created_at = Column(DateTime, server_default=func.now(), doc="fecha de creación")
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(),
                        doc="fecha de última actualización")

    def __init__(self, brand, license_plate, model, kilometers, color, displacement, fuel):
        self.brand = brand,
        self.license_plate = license_plate,
        self.model = model,
        self.kilometers = kilometers,
        self.color = color,
        self.displacement = displacement,
        self.fuel = fuel,
        super().__init__()
