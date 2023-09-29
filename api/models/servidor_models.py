import mysql
from ..database import DatabaseConnection

from flask import session

class Server:
    _keys = ['id_servidor', 'nombre', 'id_creador', 'fecha_creacion', 'ruta_img_serv']

    def __init__(self, **kwargs):
        self.id_servidor = kwargs.get('id_servidor', None)
        self.nombre = kwargs.get('nombre', None)
        self.id_usuario = kwargs.get('id_usuario', None)
        self.id_creador = kwargs.get('id_creador', None)  
        self.fecha_creacion = kwargs.get('fecha_creacion', None)
        self.ruta_img_serv = kwargs.get('ruta_img_serv', None)

    def serialize(self):
        # Método para serializar el objeto del servidor a un diccionario
        return {
            'id_servidor': self.id_servidor,
            'nombre': self.nombre,
            'id_creador': self.id_creador,
            'fecha_creacion': self.fecha_creacion,
            'ruta_img_serv': self.ruta_img_serv,
        }

    @classmethod
    def guardar_usuario_servidor(cls, id_usuario, server_id):
        conn = DatabaseConnection.get_connection()
        cursor = conn.cursor() 

        usu_serv_query = """INSERT INTO discord.usuarios_servidores (id_usuario, id_servidor) VALUES (%s, %s);"""
        
        params = (id_usuario, server_id)  
        cursor.execute(usu_serv_query, params=params)
        conn.commit()  

        usu_serv = cursor.lastrowid

        print(f"se guardo creo {usu_serv}")
        return usu_serv

    @classmethod
    def insertar_creador(cls, id_usuario, server_id):
        conn = DatabaseConnection.get_connection()
        cursor = conn.cursor()

        creator_insert_query = """INSERT INTO discord.creador (id_usuario, id_servidor) VALUES (%s, %s);"""
        params = (id_usuario, server_id)
        cursor.execute(creator_insert_query, params=params)
        conn.commit()

        creador_id = cursor.lastrowid

        return creador_id

    @classmethod
    def actualizar_server(cls, id_usuario, server_id):
        creador_id = cls.insertar_creador(id_usuario, server_id)

        query = """UPDATE discord.servidores SET id_creador = %s WHERE id_servidor = %s;"""

        params = (creador_id, server_id)
        DatabaseConnection.execute_query(query, params=params)
        
        print(f"se actualizo el creador {creador_id} del servidor {server_id} exitosamente")

        return True


#Logica de Servidor
#Creacion de un nuevo Servidor 
    @classmethod
    def create_server(cls, server):
        conn = DatabaseConnection.get_connection()
        try:
            cursor = conn.cursor()

            insert_query = """INSERT INTO discord.servidores (nombre, fecha_creacion, ruta_img_serv) VALUES (%s, NOW(), 'ruta-imagen-serv');"""
            values = (server.nombre,)

            cursor.execute(insert_query, params=values)
            conn.commit()

            nombre_servidor = server.nombre
            server_id = cursor.lastrowid
            
            cls.guardar_usuario_servidor(server.id_usuario, server_id)

            cls.actualizar_server(server.id_usuario, server_id)

        except Exception as e:
            return {"Error": str(e)}

        return server_id

#Obtener un Servidor 
    @classmethod 
    def get_servers(cls, id_usuario):
        query = ("""SELECT SERV.nombre FROM discord.usuarios AS USU INNER JOIN discord.usuarios_servidores AS USUSERV ON USU.id_usuario = USUSERV.id_usuario INNER JOIN discord.servidores AS SERV ON USUSERV.id_servidor = SERV.id_servidor WHERE USU.id_usuario = %s;""")
        params = (id_usuario,)
        servers = DatabaseConnection.fetch_all(query, params=params)

        return servers

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















