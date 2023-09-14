from flask import Blueprint

from ..controllers.signup_controller import SignUpController

signup_bp = Blueprint('signup_bp', __name__)

signup_bp.route('/', methods=['POST'])(SignUpController.signup)
