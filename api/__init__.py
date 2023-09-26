from flask import Flask
from flask_cors import CORS
from config import Config

from .routes.messages_bp import messages_bp
from .routes.login_bp import login_bp
from .routes.signup_bp import signup_bp
from .routes.server_bp import server_bp
from .routes.channel_bp import channel_bp

from .database import DatabaseConnection

def init_app():
    """Crea y configura la aplicación Flask"""
    
    app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)
    
    CORS(app, supports_credentials=True)

    #CORS(app, resources={r"/*": {"origins": "*"}})

    #CORS(app, resources={r"/server/*": {"origins": "http://127.0.0.1:5500"}})


    app.config.from_object(
        Config
    )

    DatabaseConnection.set_config(app.config)

    app.register_blueprint(messages_bp, url_prefix='/messages')
    
    app.register_blueprint(login_bp, url_prefix='/login')

    app.register_blueprint(signup_bp, url_prefix='/signup')

    app.register_blueprint(server_bp, url_prefix='/server')

    app.register_blueprint(channel_bp, url_prefix='/channels')

    return app