
import mysql
from database import DatabaseConnection

class Servidor:
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
def crear_servidor(cls, servidor):
        try:
            conn = DatabaseConnection.connect() 
            cursor = conn.cursor()

            insert_query = "INSERT INTO servidores (name, description, owner_id) VALUES (%s, %s, %s)"
            values = (servidor.name, servidor.description, servidor.owner_id)

            cursor.execute(insert_query, values)
            conn.commit()

            servidor.server_id = cursor.lastrowid

            cursor.close()
            conn.close()

            return servidor 
        except Exception as error:
            print(f"Error al crear el servidor: {error}")
            return None

#Obtener Servidor por id. 

@classmethod
def obtener_servidor_por_id(cls, server_id):
        try:
            conn = DatabaseConnection.connect()  
            cursor = conn.cursor(dictionary=True)

            select_query = "SELECT * FROM servidores WHERE server_id = %s"
            cursor.execute(select_query, (server_id,))
            servidor = cursor.fetchone()

            cursor.close()
            conn.close()

            if servidor:
                return cls(**servidor) 
            else:
                return None
        except Exception as error:
            print(f"Error al obtener el servidor: {error}")
            return None
#Actualizar o Modificar un Servidor         
@classmethod
def actualizar_servidor(cls, servidor):
        try:
            conn = DatabaseConnection.connect()  
            cursor = conn.cursor()

            update_query = "UPDATE servidores SET name = %s, description = %s WHERE server_id = %s"
            values = (servidor.name, servidor.description, servidor.server_id)

            cursor.execute(update_query, values)
            conn.commit()

            cursor.close()
            conn.close()

            return True  
        except Exception as error:
            print(f"Error al actualizar el servidor: {error}")
            return False
        
#Elimiar un Servidor
@classmethod
def eliminar_servidor(cls, server_id):
        try:
            conn = DatabaseConnection.connect() 
            cursor = conn.cursor()

            delete_query = "DELETE FROM servidores WHERE server_id = %s"
            values = (server_id,)

            cursor.execute(delete_query, values)
            conn.commit()

            cursor.close()
            conn.close()

            return True  
        except Exception as error:
            print(f"Error al eliminar el servidor: {error}")
            return False 
