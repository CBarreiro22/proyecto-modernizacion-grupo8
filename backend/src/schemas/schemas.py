new_car_schema_v1 = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "marca": {
            "type": "string"
        },
        "placa": {
            "type": "string"
        },
        "modelo": {
            "type": "integer"
        },
        "kilometros": {
            "type": "integer"
        },
        "color": {
            "type": "string"
        },
        "cilindraje": {
            "type": "integer"
        },
        "tipo_combustible": {
            "type": "string"
        }
    },
    "required": [
        "marca",
        "placa",
        "modelo",
        "kilometros",
        "color",
        "cilindraje",
        "tipo_combustible"
    ]
}
