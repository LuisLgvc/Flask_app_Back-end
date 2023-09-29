from ..database import DatabaseConnection

from flask import jsonify, session
from datetime import datetime


class Messages:
    def __init__(self, id_mensaje = None, id_usuario = None, contenido = None, fecha_hora = None, id_canal = None, nombre_canal = None):
        self.id_mensaje = id_mensaje
        self.id_usuario = id_usuario
        self.contenido = contenido
        self.fecha_hora = fecha_hora
        self.id_canal = id_canal
        self.nombre_canal = nombre_canal

    def formatted_response(self):
        return {
            'id_mensaje': int(self.id_mensaje),
            'usuario': str(self.id_usuario),
            'contenido': str(self.contenido),
            'fecha_hora': str(self.fecha_hora),
            'id_canal': int(self.id_canal),
        }

    @classmethod
    def get_channel_id_by_name(cls, nombre_canal):
        query = """SELECT CAN.id_canal FROM discord.canal AS CAN WHERE CAN.nombre = %s;"""
        params = (nombre_canal,)
        response = DatabaseConnection.fetch_one(query, params=params)
        if response is not None:
            return response[0]
        return None

    @classmethod
    def create_message(cls, message):
        query = """INSERT INTO discord.mensajes (contenido, id_usuario, fecha_hora, id_canal) VALUES (%s, %s, CURTIME(), %s);"""
        id_canal = cls.get_channel_id_by_name(message.nombre_canal)
        params = (message.contenido, message.id_usuario, id_canal)
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def get_messages(cls, messages):
        query = """SELECT MSG.id_mensaje, USU.usuario, MSG.contenido, DATE_FORMAT(MSG.fecha_hora, '%d-%m-%Y %H:%i'), MSG.id_canal FROM discord.mensajes AS MSG INNER JOIN discord.canal AS CAN ON MSG.id_canal = CAN.id_canal INNER JOIN discord.usuarios AS USU ON MSG.id_usuario = USU.id_usuario WHERE CAN.nombre = %s;"""
        params = (messages.nombre_canal,)
        responses = DatabaseConnection.fetch_all(query, params=params)
        all_messages = []

        if responses is not None:
            for response in responses:
                all_messages.append(cls(*response))
            return all_messages
        return None

    @classmethod
    def update_message(cls, id_mensaje, message):
        query = """UPDATE discord.mensajes AS MSG SET MSG.contenido = %s, MSG.fecha_hora = DATETIME() WHERE MSG.id_mensaje = %s;"""

        params = message.contenido, id_mensaje
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def delete_message(cls, id_mensaje):
        query = """DELETE FROM discord.mensajes WHERE mensajes.id_mensaje = %s;"""

        params = (id_mensaje,)

        DatabaseConnection.execute_query(query, params=params)
