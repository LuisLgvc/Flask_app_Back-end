
import mysql
from database import DatabaseConnection

class Server:
    def __init__(self, **kwargs):
        self.server_id = kwargs.get('server_id')
        self.name = kwargs.get('name')
        self.description = kwargs.get('description', '')
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
        conn = DatabaseConnection.connect()
        cursor = conn.cursor()

        insert_query = "INSERT INTO servers (name, description) VALUES (%s, %s)"
        values = (server.name, server.description)

        cursor.execute(insert_query, values)
        conn.commit()

        server_id = cursor.lastrowid
        cursor.close()
        conn.close()

        return server_id
#Obtener un Servidor 
    @classmethod
    def get_servers(cls):
        conn = DatabaseConnection.connect()
        cursor = conn.cursor(dictionary=True)

        select_query = "SELECT * FROM servers"
        cursor.execute(select_query)
        servers = cursor.fetchall()

        cursor.close()
        conn.close()

        return [cls(**server) for server in servers]
#Actualizar un Servidor     
    @classmethod
    def update_server(cls, server_id, new_data):
        conn = DatabaseConnection.connect()
        cursor = conn.cursor()

        update_query = "UPDATE servers SET name=%s, description=%s WHERE server_id=%s"
        values = (new_data['name'], new_data['description'], server_id)

        cursor.execute(update_query, values)
        conn.commit()

        cursor.close()
        conn.close()

        return True
#Borrar un Servidor 
    @classmethod
    def delete_server(cls, server_id):
        conn = DatabaseConnection.connect()
        cursor = conn.cursor()

        delete_query = "DELETE FROM servers WHERE server_id=%s"
        cursor.execute(delete_query, (server_id,))
        conn.commit()

        cursor.close()
        conn.close()

        return True
