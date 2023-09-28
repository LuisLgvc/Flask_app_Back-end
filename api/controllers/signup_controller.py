from ..models.signup_models import SignUp

from flask import jsonify, request, session


class SignUpController:

    @classmethod  # ENDPOINT de prueba para signup http://127.0.0.1:5000/signup
    def signup(cls):
        """Realiza el llamado al metodo para realizar el signup"""
        data = request.json
        user = SignUp(
            name=data.get('nombre'),
            lastname=data.get('apellido'),
            username=data.get('usuario'),
            email=data.get('email'),
            password=data.get('contraseña'),
            date_of_birth=data.get('fecha_nac'),
            route_img=data.get('ruta_img_usu')
        )
        response = SignUp.signup(user)
        if response:
            return response.serialize(), 200
        else:
            return {"message": "ha ocurrido un error"}, 401
