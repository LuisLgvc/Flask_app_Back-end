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
#Creacion de un nuevo Canal 
    # @classmethod
    # def create_channel(cls, channel):
    #     # En los metodos como estos tengo que utilizar el conn y cursor para asi poder obtener el id del servidor al que pertenece el canal que se esta creando con lastrowid ya que no se hacerlo con DatabaseConnection
        
    #     conn = DatabaseConnection.get_connection()
    #     cursor = conn.cursor()

    #     insert_query = """INSERT INTO discord.canal (nombre, id_servidor, id_mensaje) VALUES (%s, %s, %s);"""
    #     values = (channel.nombre, channel.id_servidor, channel.id_mensaje)

    #     cursor.execute(insert_query, params=values)
    #     conn.commit()

    #     channel_id = cursor.lastrowid
    #     cursor.close()
    #     conn.close()

    #     return channel_id

    #

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

#Obtener Canales de un Servidor  
    # @classmethod
    # def get_channels_by_server(cls, server_id):
    #     conn = DatabaseConnection.get_connection()
    #     cursor = conn.cursor(dictionary=True)

    #     select_query = "SELECT * FROM discord.canal WHERE id_servidor = %s"
    #     cursor.execute(select_query, (server_id,))
    #     channels = cursor.fetchall()

    #     cursor.close()
    #     conn.close()

    #     return [cls(**channel) for channel in channels]

# PRUEBA de obtencion de canales a traves de un endopoint con parametros tratando de que esos se concatenen en la url desde JS para que asi no haya que hacer un JSON

    

#trato de obtener los canales del servidor que presione recien, tengo que ver en JS si puedo obtener el nombre presionado y con eso ya llamo al metodo este que lo busca a traves del nombre
    @classmethod
    def get_channels_by_server_name(cls, nombre_servidor):
        select_query = """SELECT CAN.nombre FROM discord.canal AS CAN INNER JOIN discord.servidores AS SERV ON CAN.id_servidor = SERV.id_servidor WHERE SERV.nombre = %s;"""
        params = (nombre_servidor,)
        response = DatabaseConnection.fetch_all(select_query, params=params)
        # channels = cursor.fetchall()

        # cursor.close()
        # conn.close()

        # return [cls(**channel) for channel in channels]
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
#Actualizar un Canal 
    # @classmethod
    # def update_channel(cls, channel_id, new_data):
    #     conn = DatabaseConnection.get_connection()
    #     cursor = conn.cursor()

    #     update_query = "UPDATE discord.canal SET name = %s WHERE channel_id = %s"
    #     values = (new_data['name'], channel_id)

    #     cursor.execute(update_query, values)
    #     conn.commit()

    #     cursor.close()
    #     conn.close()

    #     return True
#Borrar un Canal 
    # @classmethod
    # def delete_channel(cls, channel_id):
    #     conn = DatabaseConnection.get_connection()
    #     cursor = conn.cursor()

    #     delete_query = "DELETE FROM channels WHERE channel_id = %s"
    #     cursor.execute(delete_query, (channel_id,))
    #     conn.commit()

    #     cursor.close()
    #     conn.close()

    #     return True
