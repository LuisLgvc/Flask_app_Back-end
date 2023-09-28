from flask import jsonify, request
from ..models.usuario_models import Usuario

class UsuarioController:
    
    @classmethod #Endpoint de Prueba http://127.0.0.1:5000/api/usuarios METODO POST
    def crear_usuario(cls):
        data = request.json
        nuevo_usuario = Usuario(
            username=data.get('usuario', None),
            password=data.get('contraseña', None),
            email=data.get('email', None),
            first_name=data.get('nombre', None),
            last_name=data.get('apellido', None),
            date_of_birth=data.get('fecha_nac', None),
            avatar_url=data.get('ruta_img_usu', None)
        )

        print(username)

        user_id = Usuario.crear_usuario(nuevo_usuario)

        if user_id:
            return jsonify({"user_id": user_id}), 201
        else:
            return jsonify({"message": "Error al crear el usuario"}), 500

    @classmethod #Endpoint de Prueba http://127.0.0.1:5000/api/usuarios METODO GET
    def get_usuarios(cls):
        usuarios = Usuario.obtener_usuarios()
        if usuarios:
            return jsonify([usuario.serialize() for usuario in usuarios]), 200
        else:
            return jsonify({"message": "No se encontraron usuarios"}), 404
    
    @classmethod #Endpoint de Prueba http://127.0.0.1:5000/api/usuarios/1 METODO GET
    def obtener_usuario_por_id(cls, user_id):
        usuario = Usuario.obtener_usuario_por_id(user_id)
        if usuario:
            return jsonify(usuario.serialize()), 200
        else:
            return jsonify({"message": "Usuario no encontrado"}), 404

    @classmethod #Endpoint de Prueba http://127.0.0.1:5000/api/usuarios/1 METODO PUT
    def actualizar_usuario(cls, user_id):
        data = request.json
        if Usuario.actualizar_usuario(user_id, data):
            return jsonify({"message": "Usuario actualizado exitosamente"}), 200
        else:
            return jsonify({"message": "Error al actualizar el usuario"}), 500

    @classmethod #Endpoint de Prueba http://127.0.0.1:5000/api/usuarios/1 METODO DELETE
    def eliminar_usuario(cls, user_id):
        if Usuario.eliminar_usuario(user_id):
            return jsonify({"message": "Usuario eliminado exitosamente"}), 200
        else:
            return jsonify({"message": "Error al eliminar el usuario"}), 500
