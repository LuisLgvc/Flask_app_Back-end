import mysql
from database import DatabaseConnection

class Channel:
    def __init__(self, **kwargs):
        self.channel_id = kwargs.get('channel_id')
        self.server_id = kwargs.get('server_id')
        self.name = kwargs.get('name')

    def serialize(self):
        # Método para serializar el objeto del canal a un diccionario
        channel_dict = {
            'channel_id': self.channel_id,
            'server_id': self.server_id,
            'name': self.name,
        }
        return channel_dict
#Creacion de un nuevo Canal 
    @classmethod
    def create_channel(cls, channel):
        conn = DatabaseConnection.connect()
        cursor = conn.cursor()

        insert_query = "INSERT INTO channels (server_id, name) VALUES (%s, %s)"
        values = (channel.server_id, channel.name)

        cursor.execute(insert_query, values)
        conn.commit()

        channel_id = cursor.lastrowid
        cursor.close()
        conn.close()

        return channel_id
#Obtener Canales de un Servidor  
    @classmethod
    def get_channels_by_server(cls, server_id):
        conn = DatabaseConnection.connect()
        cursor = conn.cursor(dictionary=True)

        select_query = "SELECT * FROM channels WHERE server_id = %s"
        cursor.execute(select_query, (server_id,))
        channels = cursor.fetchall()

        cursor.close()
        conn.close()

        return [cls(**channel) for channel in channels]
#Obtener Canal por su ID
    @classmethod
    def get_channel_by_id(cls, channel_id):
        conn = DatabaseConnection.connect()
        cursor = conn.cursor(dictionary=True)

        select_query = "SELECT * FROM channels WHERE channel_id = %s"
        cursor.execute(select_query, (channel_id,))
        channel = cursor.fetchone()

        cursor.close()
        conn.close()

        return cls(**channel) if channel else None
#Actualizar un Canal 
    @classmethod
    def update_channel(cls, channel_id, new_data):
        conn = DatabaseConnection.connect()
        cursor = conn.cursor()

        update_query = "UPDATE channels SET name = %s WHERE channel_id = %s"
        values = (new_data['name'], channel_id)

        cursor.execute(update_query, values)
        conn.commit()

        cursor.close()
        conn.close()

        return True
#Borrar un Canal 
    @classmethod
    def delete_channel(cls, channel_id):
        conn = DatabaseConnection.connect()
        cursor = conn.cursor()

        delete_query = "DELETE FROM channels WHERE channel_id = %s"
        cursor.execute(delete_query, (channel_id,))
        conn.commit()

        cursor.close()
        conn.close()

        return True
