from ..models.signup_models import SignUp

from flask import jsonify, request, session


class SignUpController:

    @classmethod  # ENDPOINT de prueba para signup http://127.0.0.1:5000/signup
    def signup(cls):
        """Realiza el llamado al metodo para realizar el signup"""
        data = request.json
        user = SignUp(
            name=data.get('name'),
            lastname=data.get('lastname'),
            username=data.get('username'),
            email=data.get('email'),
            password=data.get('password'),
            date_of_birth=data.get('date_of_birth'),
            route_img=data.get('route_img')
        )

        if SignUp.signup(user):
            return {"message": "Registro exitoso"}, 200
        else:
            return {"message": "ha ocurrido un error"}, 401
