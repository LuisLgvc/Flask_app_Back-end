from flask import Blueprint
from ..controllers.servidor_controller import ServerController

server_bp = Blueprint('server_bp', __name__)

server_bp.route('/', methods=['POST'])(ServerController.create_server)
server_bp.route('/', methods=['GET'])(ServerController.get_servers)
server_bp.route('/sinid', methods=['GET'])(ServerController.get_server_by_id)
server_bp.route('/image', methods=['GET'])(ServerController.get_image_server)
# server_bp.route('/servers/<int:server_id>', methods=['PUT'])(ServerController.update_server)
# server_bp.route('/servers/<int:server_id>', methods=['DELETE'])(ServerController.delete_server)
