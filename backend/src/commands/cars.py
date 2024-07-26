import logging

from sqlalchemy.exc import IntegrityError

from src.commands.base_command import BaseCommand
from src.errors.errors import duplicate_error, internal_server_error
from src.models.car import Car, newCarJsonSchema, CarJsonSchema
from src.models.model import db_session, init_db

init_db()


class Cars(BaseCommand):
    def __init__(self, data):
        self.brand = data.get('marca')
        self.license_plate = data.get('placa')
        self.model = data.get('modelo')
        self.kilometers = data.get('kilometros')
        self.color = data.get('color')
        self.displacement = data.get('cilindraje')
        self.fuel = data.get('tipo_combustible')


    def create_car(self):
        try:

            with db_session() as session:

                new_car = Car(
                    brand=self.brand,
                    license_plate=self.license_plate,
                    model=self.model,
                    kilometers=self.kilometers,
                    color=self.color,
                    displacement=self.displacement,
                    fuel=self.fuel
                )
            session.add(new_car)
            session.commit()
            logging.info(f'car with license_plate: {self.license_plate} created successfully')
            car_schema = newCarJsonSchema()
            return car_schema.dump(new_car)
        except IntegrityError as e:
            logging.error("Error saving coach: %s", str(e))
            raise duplicate_error("Duplicate key error occurred")
        except Exception as e:
            logging.error("Error saving car: %s", str(e))
            raise internal_server_error(e)

    def list_cars(self, filters):
        try:
            with db_session() as session:
                query = session.query(Car)
                if 'placa' in filters:
                    query = query.filter(Car.license_plate == filters['placa'])
                if 'cilindraje' in filters:
                    query = query.filter(Car.displacement == filters['cilindraje'])
                if 'id' in filters:
                    query = query.filter(Car.id == filters['id'])
                if 'kilometros' in filters:
                    query = query.filter(Car.kilometers == filters['kilometros'])
                if 'marca' in filters:
                    query = query.filter(Car.brand == filters['marca'])
                if 'modelo' in filters:
                    query = query.filter(Car.model == filters['modelo'])
                if 'tipo_combustible' in filters:
                    query = query.filter(Car.fuel == filters['tipo_combustible'])
                cars = query.all()
                car_schema = CarJsonSchema(many=True)
                return car_schema.dump(cars)
        except Exception as e:
            logging.error("Error listing cars: %s", str(e))
            raise internal_server_error(e)

    def execute(self):
        return self.create_car()
