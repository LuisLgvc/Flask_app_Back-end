from flask import Blueprint
from usuario_controller import UsuarioController

usuario_bp = Blueprint('usuario_bp', __name__)

usuario_bp.route('/usuarios', methods=['GET'])(UsuarioController.get_usuarios)
usuario_bp.route('/usuarios', methods=['POST'])(UsuarioController.crear_usuario)
usuario_bp.route('/usuarios/<int:user_id>', methods=['GET'])(UsuarioController.obtener_usuario_por_id)
usuario_bp.route('/usuarios/<int:user_id>', methods=['PUT'])(UsuarioController.actualizar_usuario)
usuario_bp.route('/usuarios/<int:user_id>', methods=['DELETE'])(UsuarioController.eliminar_usuario)
