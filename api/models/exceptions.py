from flask import jsonify

class CustomException(Exception):

    def __init__(self, status_code, name = "Custom Error", description = 'Error'): 
        super().__init__()
        self.description = description
        self.name = name
        self.status_code = status_code

    def get_response(self):
        response = jsonify({
            'error': {
                'code': self.status_code,
                'name': self.name,
                'description': self.description,
            }
        })
        response.status_code = self.status_code
        return response
    
class UsuarioNoEncontrado(CustomException):
    def __init__(self, description='Usuario no encontrado'):
        super().__init__(status_code=404, name='Usuario No Encontrado', description=description)

class CrearUsuarioError(CustomException):
    def __init__(self, description='Error al crear el usuario'):
        super().__init__(status_code=400, name='Crear Usuario Error', description=description)

class ActualizarUsuarioError(CustomException):
    def __init__(self, description='Error al actualizar el usuario'):
        super().__init__(status_code=400, name='Actualizar Usuario Error', description=description)

class EliminarUsuarioError(CustomException):
    def __init__(self, description='Error al eliminar el usuario'):
        super().__init__(status_code=400, name='Eliminar Usuario Error', description=description)