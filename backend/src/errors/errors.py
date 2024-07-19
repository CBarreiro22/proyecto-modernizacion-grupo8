class ApiError(Exception):
    code = 422
    description = "Default message"


class internal_server_error(ApiError):
    code = 500
    description = "error en la aplicación"

    def __init__(self, error):
        self.description = f"{self.description}: {str(error)}"
        self.error = error

class duplicate_error(ApiError):
    code = 409
    description = "El automovil ya existe"

    def __init__(self, error):
        self.description = f"{self.description}: {str(error)}"
        self.error = error

class json_invalid_new_Service(ApiError):
    code = 400
    description = "el mensaje no cumple con los requerimientos"

    def __init__(self, error):
        self.description = f"{self.description}: {str(error)}"
        self.error = error
