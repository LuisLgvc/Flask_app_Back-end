from ..database import DatabaseConnection

from flask import jsonify, session
from datetime import datetime

class Messages:
    def __init__(self, id_mensaje = None, id_usuario = None, contenido = None, fecha_hora = None, id_canal = None):
        self.id_mensaje = id_mensaje
        self.id_usuario = id_usuario
        self.contenido = contenido
        self.fecha_hora = fecha_hora
        # self.fecha = fecha
        # self.hora = hora
        self.id_canal = id_canal    

    def formatted_response(self):
        return {
            'id_mensaje': int(self.id_mensaje),
            'id_usuario': str(self.id_usuario),
            'contenido': str(self.contenido),
            'fecha_hora': str(self.fecha_hora),
            # 'fecha': str(self.fecha),
            # 'hora': str(self.hora),
            'id_canal': int(self.id_canal),
        }

    @classmethod
    def get_messages(cls, messages):
        query = """SELECT MSG.id_mensaje, MSG.id_usuario, MSG.contenido, DATE_FORMAT(MSG.fecha_hora, '%d-%m-%Y %H:%i:%s'), MSG.id_canal FROM discord.mensajes AS MSG INNER JOIN discord.canal AS CAN ON MSG.id_canal = CAN.id_canal WHERE CAN.nombre = %s;"""
        params = (messages.id_canal,)
        print(params)
        responses = DatabaseConnection.fetch_all(query, params=params)
        all_messages = []

        if responses is not None:
            for response in responses:
                all_messages.append(cls(*response))
            return all_messages
        return None

    @classmethod
    def create_message(cls, message):
        query = """INSERT INTO discord.mensajes (contenido, id_usuario, fecha_hora, id_canal) VALUES (%s, %s, CURTIME(), %s);"""
        #id_canal = cls.get_channel_id_by_name(nombre_canal)
        params = (message.contenido, id_usuario, id_canal)
        DatabaseConnection.execute_query(query, params=params)

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

