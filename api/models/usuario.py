#Creacion de Modelo Usuario 

from flask import jsonify
from database import DatabaseConnection

class Usuario:
    def __init__(self, **kwargs):
        self.user_id = kwargs.get('user_id')
        self.username = kwargs.get('username')
        self.password = kwargs.get('password')
        self.email = kwargs.get('email')
        self.first_name = kwargs.get('first_name')
        self.last_name = kwargs.get('last_name')
        self.date_of_birth = kwargs.get('date_of_birth')
        self.creation_date = kwargs.get('creation_date')
        self.last_login = kwargs.get('last_login')
        self.status_id = kwargs.get('status_id')
        self.avatar_url = kwargs.get('avatar_url', None) 

    def serialize(self):
        # Serializa el objeto Usuario en un diccionario
        user_dict = {
            'user_id': self.user_id,
            'username': self.username,
            'password': self.password,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'date_of_birth': self.date_of_birth,
            'creation_date': self.creation_date,
            'last_login': self.last_login,
            'status_id': self.status_id,
            'avatar_url': self.avatar_url
        }
        return user_dict

# Crear un usuario usando **kwargs
kwargs = {
    'user_id': 1,
    'username': 'ejemplo_usuario',
    'password': 'contraseña123',
    'email': 'usuario@ejemplo.com',
    'first_name': 'Nombre',
    'last_name': 'Apellido',
    'date_of_birth': '1990-01-01',
    'creation_date': '2023-09-08',
    'last_login': '2023-09-08',
    'status_id': 1,
    'avatar_url': 'https://example.com/avatar.png'
}

usuario = Usuario(**kwargs)

# Serializar el usuario a un diccionario
usuario_dict = usuario.serialize()

# Imprimir el diccionario serializado
print(usuario_dict)






