import mysql
from ..database import DatabaseConnection

from flask import session

class Server:
    def __init__(self, **kwargs):
        self.server_id = kwargs.get('server_id')
        self.name = kwargs.get('nombre', None)
        self.description = kwargs.get('descripcion', None)
        self.owner_id = kwargs.get('owner_id')  # ID del usuario que creó el servidor
        self.members = []  # Lista de usuarios miembros del servidor
        self.channels = []  # Lista de canales en el servidor

    def serialize(self):
        # Método para serializar el objeto del servidor a un diccionario
        server_dict = {
            'server_id': self.server_id,
            'name': self.name,
            'description': self.description,
            'owner_id': self.owner_id,
            'members': [member.serialize() for member in self.members],  # Serializar usuarios miembros
            'channels': [channel.serialize() for channel in self.channels],  # Serializar canales
        }
        return server_dict

#Logica de Servidor
#Creacion de un nuevo Servidor 
    @classmethod
    def create_server(cls, server):
        conn = DatabaseConnection.get_connection()
        try:
            cursor = conn.cursor()

            insert_query = """INSERT INTO discord.servidores (nombre, descripcion, id_canal, fecha_creacion, ruta_img_serv) VALUES (%s, %s, 4, NOW(), 'ruta-imagen-serv');"""
            values = (server.name, server.description)

            cursor.execute(insert_query, params=values)
            conn.commit()

            nombre_servidor = server.name
            server_id = cursor.lastrowid
            cursor.close()

            cursor = conn.cursor()

            query = """INSERT INTO discord.creador (id_usuario, id_servidor) VALUES (%s, %s);"""
            id_usuario = session.get('id_usuario', None)
            params = (id_usuario, server_id)
            DatabaseConnection.execute_query(query, params=params)

            query = """SELECT id_creador FROM discord.creador WHERE id_servidor = %s;"""
            params = (server_id,)
            creator_id = DatabaseConnection.fetch_one(query, params=params)

            update_query = """UPDATE discord.servidores SET id_creador = %s WHERE id_servidor = %s;"""
            params = (creator_id[0], server_id)
            DatabaseConnection.execute_query(update_query, params=params)

        except Exception as e:
            return {"Error": str(e)}

        return server_id

#Obtener un Servidor 
    @classmethod # Obtengo los servidores a traves del id que guarde en la sesion (session['id_usuario'])
    def get_servers(cls, id_usuario):
        query = ("""SELECT SERV.nombre FROM discord.usuarios AS USU INNER JOIN discord.usuarios_servidores AS USUSERV ON USU.id_usuario = USUSERV.id_usuario INNER JOIN discord.servidores AS SERV ON USUSERV.id_servidor = SERV.id_servidor WHERE USU.id_usuario = %s;""")
        params = (id_usuario,)
        servers = DatabaseConnection.fetch_all(query, params=params)

        all_servers = [dict(servidor=server[0]) for server in servers]

        return all_servers

    def get_servers_without_id(cls):
        query = ("""SELECT SERV.nombre FROM discord.servidores AS SERV;""")
        serverss = DatabaseConnection.fetch_all(query)

        all_servers = [dict(servidor=server[0]) for server in serverss]
        
        return all_servers

    @classmethod
    def get_image_server(cls):
        query = """SELECT SERV.ruta_img_serv FROM discord.servidores AS SERV;"""
        
        image_server = DatabaseConnection.fetch_one(query)

        img_servers = dict(imagen=image_server[0])

        return img_servers















