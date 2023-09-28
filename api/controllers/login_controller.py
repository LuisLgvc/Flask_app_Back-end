from ..models.login_models import Login

from flask import jsonify, request, session


class LoginController:
    @classmethod
    def login(self):
        """Realiza el llamado al metodo para realizar el login"""
        data = request.json
        user = Login(
            email=data.get('email'),
            password=data.get('password'),
        )
        response = Login.login(user)
        if response:
            session['id_usuario'] = response.id_usuario
            session['usuario'] = response.usuario
            session['email'] = response.email
            session['password'] = response.password
            return response.serialize(), 200

        return {"message": "Usuario o contraseña incorrectos"}, 401

    @classmethod  # ENDPOINT de prueba para http://127.0.0.1:5000/login/logout
    def logout(cls):
        session.pop('id_usuario', None)
        session.pop('usuario', None)
        session.pop('email', None)
        session.pop('password', None)
        return {"message": "Sesion cerrada"}, 200
