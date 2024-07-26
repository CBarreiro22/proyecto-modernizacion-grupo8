from marshmallow import fields, Schema
from sqlalchemy import Column, String, Text, Integer, Boolean, REAL, DateTime, func

from .model import Model


class newCarJsonSchema(Schema):
    id = fields.String()


class CarJsonSchema(Schema):
    id = fields.String()
    marca = fields.String(attribute="brand")
    placa = fields.String(attribute="license_plate")
    modelo = fields.Integer(attribute="model")
    kilometros = fields.Integer(attribute="kilometers")
    color = fields.String()
    cilindraje = fields.Integer(attribute="displacement")
    tipo_combustible = fields.String(attribute="fuel")
    created_at = fields.String(attribute="created_at")
    updated_at = fields.String(attribute="updated_at")


class Car(Model):
    __tablename__ = 'car'

    brand = Column(String, doc="marca del automovil")
    license_plate = Column(String, nullable=False, unique=True, doc="Placa del vehículo")
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
