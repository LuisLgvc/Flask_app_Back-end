from flask import Blueprint, request, jsonify
from models import Usuario

usuario_bp = Blueprint('usuario_bp', __name__)

@usuario_bp.route('/usuarios', methods=['POST'])
def crear_usuario():
    data = request.json
    nuevo_usuario = Usuario(**data)
    user_id = Usuario.crear_usuario(nuevo_usuario)
    if user_id is not None:
        return jsonify({'user_id': user_id}), 201
    return jsonify({'message': 'Error al crear el usuario'}), 500

@usuario_bp.route('/usuarios/<int:user_id>', methods=['GET'])
def obtener_usuario(user_id):
    usuario = Usuario.obtener_usuario_por_id(user_id)
    if usuario:
        return jsonify(usuario.serialize()), 200
    return jsonify({'message': 'Usuario no encontrado'}), 404

@usuario_bp.route('/usuarios/<int:user_id>', methods=['PUT'])
def actualizar_usuario(user_id):
    data = request.json
    usuario = Usuario.obtener_usuario_por_id(user_id)
    if usuario:
        usuario.username = data.get('username', usuario.username)
        usuario.password = data.get('password', usuario.password)
        usuario.email = data.get('email', usuario.email)
        usuario.first_name = data.get('first_name', usuario.first_name)
        usuario.last_name = data.get('last_name', usuario.last_name)
        usuario.date_of_birth = data.get('date_of_birth', usuario.date_of_birth)
        usuario.creation_date = data.get('creation_date', usuario.creation_date)
        usuario.last_login = data.get('last_login', usuario.last_login)
        usuario.status_id = data.get('status_id', usuario.status_id)
        usuario.avatar_url = data.get('avatar_url', usuario.avatar_url)

        if Usuario.actualizar_usuario(usuario):
            return jsonify({'message': 'Usuario actualizado'}), 200
    return jsonify({'message': 'Usuario no encontrado o error al actualizar'}), 404

@usuario_bp.route('/usuarios/<int:user_id>', methods=['DELETE'])
def eliminar_usuario(user_id):
    if Usuario.eliminar_usuario(user_id):
        return jsonify({'message': 'Usuario eliminado'}), 200
    return jsonify({'message': 'Usuario no encontrado o error al eliminar'}), 404
