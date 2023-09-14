from ..database import DatabaseConnection

from flask import jsonify, session


class Login:
    def __init__(self, **kwargs):
        self.username = kwargs.get('username', None)
        self.email = kwargs.get('email', None)
        self.password = kwargs.get('password', None)

    @classmethod
    def login(cls, user):
        query = """SELECT USU.usuario, USU.email, USU.contraseña FROM discord.usuarios AS USU WHERE USU.email = %(email)s AND USU.contraseña = %(password)s;"""
        params = user.__dict__
        response = DatabaseConnection.fetch_one(query, params=params)

        if response is not None:
            session['username'] = response[0]
            return response
        return None
