import mysql
from ..database import DatabaseConnection

class Channel:
    def __init__(self, **kwargs):
        self.id_canal = kwargs.get('id_canal')
        self.id_servidor = kwargs.get('id_servidor')
        self.nombre = kwargs.get('nombre')
        self.id_mensaje = kwargs.get('id_mensaje')
        self.nombre_servidor = kwargs.get('nombre_servidor')
        #self.id_usuario = kwargs.get('id_usuario')

    def serialize(self):
        # Método para serializar el objeto del canal a un diccionario
        channel_dict = {
            'id_canal': self.id_canal,
            'server_id': self.id_servidor,
            'name': self.nombre,
            'message_id': self.id_mensaje,
            'nombre_servidor': self.nombre_servidor,
        }
        return channel_dict

    @classmethod
    def get_server_id_by_server_name(cls, channel):
        query = """SELECT id_servidor FROM discord.servidores WHERE nombre = %s;"""
        nombre_servidor = channel.nombre_servidor
        params = (nombre_servidor,)
        server_id = DatabaseConnection.fetch_one(query, params=params)
        
        return str(server_id[0])
    
    @classmethod
    def create_channel(cls, channel):
        id_servidor = cls.get_server_id_by_server_name(channel)

        query = """INSERT INTO discord.canal (nombre, id_servidor, id_mensaje) VALUES (%s, %s, %s);"""
        params = (channel.nombre, int(id_servidor), channel.id_mensaje)

        response = DatabaseConnection.execute_query(query, params=params)

        if response is not None:

            return response

#trato de obtener los canales del servidor que presione recien, tengo que ver en JS si puedo obtener el nombre presionado y con eso ya llamo al metodo este que lo busca a traves del nombre
    @classmethod
    def get_channels_by_server_name(cls, nombre_servidor):
        select_query = """SELECT CAN.nombre FROM discord.canal AS CAN INNER JOIN discord.servidores AS SERV ON CAN.id_servidor = SERV.id_servidor WHERE SERV.nombre = %s;"""
        params = (nombre_servidor,)
        response = DatabaseConnection.fetch_all(select_query, params=params)

        return response

#Obtener Canal por su ID
    @classmethod
    def get_channel_by_id(cls, channel_id):
        conn = DatabaseConnection.get_connection()
        cursor = conn.cursor(dictionary=True)

        select_query = "SELECT * FROM discord.canal WHERE channel_id = %s"
        cursor.execute(select_query, (channel_id,))
        channel = cursor.fetchone()

        cursor.close()
        conn.close()

        return cls(**channel) if channel else None
