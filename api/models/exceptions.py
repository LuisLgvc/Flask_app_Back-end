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
#Excepciones Modelo Usuario     
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

#Excepciones Modelo Servidor 
class ServerNotFoundException(Exception):
    def __init__(self, server_id):
        super().__init__()
        self.server_id = server_id

    def get_response(self):
        return jsonify({"message": f"Servidor con ID {self.server_id} no encontrado"}), 404

class ServerUpdateException(Exception):
    def __init__(self):
        super().__init__()

    def get_response(self):
        return jsonify({"message": "Error al actualizar el servidor"}), 500

class ServerDeleteException(Exception):
    def __init__(self):
        super().__init__()

    def get_response(self):
        return jsonify({"message": "Error al eliminar el servidor"}), 500       
#Excepciones modelo Canales 
lass ChannelNotFoundException(Exception):
    def __init__(self, channel_id):
        super().__init__(f"Canal con ID {channel_id} no encontrado.")
        self.channel_id = channel_id


class ChannelCreationException(Exception):
    def __init__(self):
        super().__init__("Error al crear el canal.")


class ChannelUpdateException(Exception):
    def __init__(self, channel_id):
        super().__init__(f"Error al actualizar el canal con ID {channel_id}.")
        self.channel_id = channel_id


class ChannelDeletionException(Exception):
    def __init__(self, channel_id):
        super().__init__(f"Error al eliminar el canal con ID {channel_id}.")
        self.channel_id = channel_id

