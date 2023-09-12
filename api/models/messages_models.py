from ..database import DatabaseConnection

from flask import jsonify
from datetime import datetime

class Messages:
    def __init__(self, id_mensaje = None, id_usuario = None, contenido = None, fecha = None, hora = None, id_canal = None):
        self.id_mensaje = id_mensaje
        self.id_usuario = id_usuario
        self.contenido = contenido
        self.fecha = fecha
        self.hora = hora

        self.id_canal = id_canal    

    def formatted_response(self):
        return {
            'id_mensaje': int(self.id_mensaje),
            'id_usuario': int(self.id_usuario),
            'contenido': str(self.contenido),
            'fecha': str(self.fecha),
            'hora': str(self.hora),
            'id_canal': int(self.id_canal),
        }

    @classmethod
    def get_messages(cls, messages):
        query = """SELECT MSG.id_mensaje, MSG.id_usuario, MSG.contenido, DATE_FORMAT(MSG.fecha, '%d-%m-%Y'), TIME_FORMAT(MSG.hora, '%H:%i'), MSG.id_canal FROM discord.mensajes as MSG WHERE id_canal = %s;"""
        params = messages.id_canal,
        responses = DatabaseConnection.fetch_all(query, params=params)
        all_messages = []

        if responses is not None:
            for response in responses:
                all_messages.append(cls(*response))
            return all_messages
        return None

    @classmethod
    def create_message(cls, message):
        query = """INSERT INTO discord.mensajes (contenido, id_usuario, fecha, hora, id_canal) VALUES (%s, %s, CURDATE(), CURTIME(), %s);"""

        params = message.contenido, message.id_usuario, message.id_canal
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def update_message(cls, id_mensaje, message):
        query = """UPDATE discord.mensajes AS MSG SET MSG.contenido = %s, MSG.fecha = CURDATE(), MSG.hora = CURTIME() WHERE MSG.id_mensaje = %s;"""

        params = message.contenido, id_mensaje
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def delete_message(cls, id_mensaje):
        query = """DELETE FROM discord.mensajes WHERE mensajes.id_mensaje = %s;"""

        params = (id_mensaje,)

        DatabaseConnection.execute_query(query, params=params)

