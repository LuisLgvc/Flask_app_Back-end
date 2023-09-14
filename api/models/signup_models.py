from ..database import DatabaseConnection

from flask import jsonify, session


class SignUp:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name', None)
        self.lastname = kwargs.get('lastname', None)
        self.username = kwargs.get('username', None)
        self.email = kwargs.get('email', None)
        self.password = kwargs.get('password', None)
        self.date_of_birth = kwargs.get('date_of_birth', None)
        self.route_img = kwargs.get('route_img', None)

    @classmethod
    def signup(cls, user):
        query = """INSERT INTO discord.usuarios (nombre, apellido, usuario, email, contraseña, fecha_nac, ruta_img_usu) VALUES (%(name)s, %(lastname)s, %(username)s, %(email)s, %(password)s, %(date_of_birth)s, %(route_img)s);"""
        params = user.__dict__
        response = DatabaseConnection.execute_query(query, params=params)

        if response is not None:
            return True
        return None
