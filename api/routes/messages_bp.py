from flask import Blueprint

from ..controllers.messages_controller import MessagesController

messages_bp = Blueprint('messages_bp', __name__)

messages_bp.route('/', methods=['POST'])(MessagesController.create_message)
messages_bp.route('/', methods=['GET'])(MessagesController.get_messages)
messages_bp.route('/<int:id_message>', methods=['PUT'])(MessagesController.update_message)
messages_bp.route('/<int:id_message>', methods=['DELETE'])(MessagesController.delete_message)