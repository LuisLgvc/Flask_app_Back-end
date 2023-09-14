from flask import Blueprint

from ..controllers.login_controller import LoginController

login_bp = Blueprint('login_bp', __name__)

login_bp.route('/', methods=['GET'])(LoginController.login)
login_bp.route('/logout')(LoginController.logout)
