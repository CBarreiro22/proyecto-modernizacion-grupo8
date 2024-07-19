import logging

from flask import Blueprint, jsonify, request
from jsonschema.exceptions import ValidationError
from jsonschema.validators import validate

from src.commands.cars import Cars

headers = {
    'Content-Type': 'application/json',

}
operations_blueprint = Blueprint('operations', __name__)
logging.basicConfig(level=logging.INFO)  # Establecer el nivel de registro a INFO

@operations_blueprint.route('/health', methods=['GET'])
def health_check():
    logging.info('health check...')
    # Crear una respuesta JSON
    response_data = {'message': 'alive'}

    # Crear los encabezados para la respuesta JSON

    # Devolver la respuesta JSON con el código de estado 201
    return jsonify(response_data), 201, headers


@operations_blueprint.route ('/v1/car', methods=['POST'])
def create_car():
    logging.info('creating a car')
    json_data = request.get_json()
    created_car = Cars (data=json_data).execute()
    return jsonify(created_car), 201

