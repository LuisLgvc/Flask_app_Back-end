from flask import Blueprint
from ..controllers.channel_controller import ChannelController

channel_bp = Blueprint('channel_bp', __name__)

channel_bp.route('/', methods=['POST'])(ChannelController.create_channel)
channel_bp.route('/', methods=['GET'])(ChannelController.get_channels_by_server)
channel_bp.route('/channels/<int:channel_id>', methods=['GET'])(ChannelController.get_channel_by_id)
channel_bp.route('/channels/<int:channel_id>', methods=['PUT'])(ChannelController.update_channel)
channel_bp.route('/channels/<int:channel_id>', methods=['DELETE'])(ChannelController.delete_channel)
