from ..database import DatabaseConnection

from flask import jsonify

class Messages:
    def __init__(self, usuario = None, email = None, password = None):
        self.usuario = usuario
        self.email = email
        self.password = password

    @classmethod
    def login(cls, login_data):
        query = """SELECT USU.usuario, USU.email, USU.contraseña FROM discord.usuarios AS USU WHERE (USU.usuario = %s OR USU.email = %s) AND USU.contraseña = %s;"""
        params = (login_data.user, login_data.email, login_data.password)
        response = DatabaseConnection.fetch_all(query, params=params)

        if response is not None:
            return response
        return None