#Creacion del Modelo Usuario
import mysql.connector
from ..database import DatabaseConnection

class Usuario:
    def __init__(self, **kwargs):
        self.user_id = kwargs.get('id_usuario')
        self.username = kwargs.get('usuario')
        self.password = kwargs.get('contraseña')
        self.email = kwargs.get('email')
        self.first_name = kwargs.get('nombre')
        self.last_name = kwargs.get('apellido')
        self.date_of_birth = kwargs.get('fecha_nac')
        self.avatar_url = kwargs.get('ruta_img_usu') 

# Serializa el objeto Usuario en un diccionario
    def serialize(self):
        user_dict = {
            'user_id': self.user_id,
            'username': self.username,
            'password': self.password,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'date_of_birth': self.date_of_birth,
            'avatar_url': self.avatar_url
        }
        return user_dict
    
#Logica del Modelo Usuario 
#Creacion de un nuevo Usuario 
    @classmethod
    def crear_usuario(cls, usuario):
        conn = DatabaseConnection.get_connection()
        cursor = conn.cursor()

        insert_query = """INSERT INTO discord.usuarios (nombre, apellido, usuario, email, contraseña, fecha_nac, ruta_img_usu) VALUES (%s, %s, %s, %s, %s, %s, %s);"""

        values = (usuario.first_name, usuario.last_name, usuario.username, usuario.email, usuario.password, usuario.date_of_birth, usuario.avatar_url)
        
        print(values)

        cursor.execute(insert_query, params=values)
        conn.commit()

        user_id = cursor.lastrowid
        cursor.close()
        conn.close()

        return user_id
#Obtener un Usuario 
    @classmethod
    def obtener_usuarios(cls):
        conn = DatabaseConnection.get_connection()
        cursor = conn.cursor(dictionary=True)

        select_query = "SELECT * FROM discord.usuarios;"
        cursor.execute(select_query)
        usuarios = cursor.fetchall()

        cursor.close()
        conn.close()

        return [cls(**usuario) for usuario in usuarios]

#Obtener un Usuario por ID
    @classmethod
    def obtener_usuario_por_id(cls, user_id):
        conn = DatabaseConnection.connect()
        cursor = conn.cursor(dictionary=True)

        select_query = "SELECT * FROM usuarios WHERE user_id = %s"
        cursor.execute(select_query, (user_id,))
        usuario = cursor.fetchone()

        cursor.close()
        conn.close()

        return usuario
#Actualizar un Usuario
    @classmethod
    def actualizar_usuario(cls, user_id, nuevos_datos):
        conn = DatabaseConnection.connect()
        cursor = conn.cursor()

        update_query = "UPDATE usuarios SET username=%s, password=%s, email=%s, first_name=%s, last_name=%s, date_of_birth=%s, creation_date=%s, last_login=%s, status_id=%s, avatar_url=%s WHERE user_id=%s"
        values = (
            nuevos_datos['username'], nuevos_datos['password'],
            nuevos_datos['email'], nuevos_datos['first_name'],
            nuevos_datos['last_name'], nuevos_datos['date_of_birth'],
            nuevos_datos['creation_date'], nuevos_datos['last_login'],
            nuevos_datos['status_id'], nuevos_datos['avatar_url'], user_id
        )

        cursor.execute(update_query, values)
        conn.commit()

        cursor.close()
        conn.close()

        return True
#Eliminar un usuario
    @classmethod
    def eliminar_usuario(cls, user_id):
        conn = DatabaseConnection.connect()
        cursor = conn.cursor()

        delete_query = "DELETE FROM usuarios WHERE user_id=%s"
        cursor.execute(delete_query, (user_id,))
        conn.commit()

        cursor.close()
        conn.close()

        return True
