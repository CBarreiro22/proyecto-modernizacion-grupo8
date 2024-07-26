from flask import jsonify, Flask

from src.blueprints.operations import operations_blueprint
from src.errors.errors import ApiError
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.register_blueprint(operations_blueprint)

headers = {
    'Content-Type': 'application/json',

}
@app.errorhandler(ApiError)
def handle_exception(err):
    response = {
        "mssg": err.description,

    }
    return jsonify(response), err.code, headers
