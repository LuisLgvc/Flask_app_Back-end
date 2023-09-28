from ..database import DatabaseConnection
from flask import jsonify, session


class Login:
    _keys = ['id_usuario', 'usuario', 'email', 'password']

    def __init__(self, **kwargs):
        self.id_usuario = kwargs.get('id_usuario', None)
        self.usuario = kwargs.get('usuario', None)
        self.email = kwargs.get('email', None)
        self.password = kwargs.get('password', None)

    def serialize(self):
        return {
            'id_usuario': self.id_usuario,
            'usuario': self.usuario,
            'email': self.email,
            'password': self.password,
        }

    @classmethod
    def login(cls, user):
        query = """SELECT USU.id_usuario, USU.usuario, USU.email, USU.contraseña FROM discord.usuarios AS USU WHERE USU.email = %(email)s AND USU.contraseña = %(password)s;"""
        params = user.__dict__
        response = DatabaseConnection.fetch_one(query, params=params)

        if response:
            return cls(**dict(zip(cls._keys, response)))
        else:
            return None
