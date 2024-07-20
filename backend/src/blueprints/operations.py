import logging

from flask import Blueprint, jsonify, request
from jsonschema.exceptions import ValidationError
from jsonschema.validators import validate

from src.commands.cars import Cars
from src.errors.errors import json_invalid_new_Service
from src.schemas.schemas import new_car_schema_v1

headers = {
    'Content-Type': 'application/json',

}
operations_blueprint = Blueprint('operations', __name__)
logging.basicConfig(level=logging.INFO)  # Establecer el nivel de registro a INFO


@operations_blueprint.route('/health', methods=['GET'])
def health_check():
    """
        Endpoint para verificar el estado de salud del servicio.

        Este endpoint devuelve un mensaje indicando que el servicio está activo.

        Returns:
            response (Response): Respuesta en formato JSON con el mensaje 'alive'.
    """
    logging.info('health check...')

    response_data = {'message': 'alive'}

    return jsonify(response_data), 201, headers


@operations_blueprint.route('/v1/car', methods=['POST'])
def create_car():
    """
        Endpoint para crear un nuevo coche.

        Este endpoint recibe datos JSON de un coche, valida contra un esquema JSON
        y crea un nuevo coche utilizando el comando Cars.

        Returns:
            response (Response): Respuesta en formato JSON con los datos del coche creado.
    """
    logging.info('creating a car')
    json_data = request.get_json()
    validate_new_car_schema(json_data)
    created_car = Cars(data=json_data).execute()
    return jsonify(created_car), 201, headers


def validate_new_car_schema(json_data):
    """
    Valida los datos JSON contra el esquema de un nuevo coche.

    Args:
        json_data (dict): Datos JSON a validar.

    Raises:
        json_invalid_new_Service: Si los datos JSON no cumplen con el esquema.
    """
    try:
        validate(json_data, new_car_schema_v1)
    except ValidationError as e:
        logging.info(f'ValidationError validate_new_Service_schema {e}')
        raise json_invalid_new_Service(e)
