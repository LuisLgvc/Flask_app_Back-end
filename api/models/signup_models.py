from ..database import DatabaseConnection

from flask import jsonify


class SignUp:
    def __init__(self, name, lastname, username, email, password, fecha_nac, route_image):
        self.name = name
        self.lastname = lastname
        self.username = username
        self.email = email
        self.password = password
        self.fecha_nac = fecha_nac
        self.route_image = route_image

    def SignUp(cls, signup_data):
        query = """INSERT INTO discord.usuarios (nombre, apellido, usuario, email, contraseña, fecha_nac, ruta_img_usu) VALUES (%s, %s, %s, %s, %s, %s, %s); """
        params = (signup_data.nombre, signup_data.apellido, signup_data.usuario,
                  signup_data.contraseña, signup_data.fecha_nac, signup_data.ruta_img)
