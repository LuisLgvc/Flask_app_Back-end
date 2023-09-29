from flask import jsonify, request, session
from ..models.servidor_models import Server

class ServerController:
    
    @classmethod 
    def create_server(cls):
        data = request.json
        new_server = Server(
            nombre=data.get('nombre', None),
            id_usuario=data.get('id_usuario', None),
        )

        server_id = Server.create_server(new_server)

        if server_id:
            return jsonify({"exito": server_id}), 200
        else:
            return jsonify({"message": "Error al crear el servidor"}), 500

    @classmethod 
    def get_servers(cls, id_usuario):
        
        servers = Server.get_servers(id_usuario)

        if servers:
            return jsonify(servers), 200
        else:
            return jsonify({"message": "No se encontraron servidores"}), 404


    @classmethod 
    def get_server_by_id(cls):
        server = Server.get_servers_without_id(cls)
        if server:
            return server, 200
        else:
            return jsonify({"message": "Servidor no encontrado"}), 404

    @classmethod
    def get_image_server(cls):
        server = Server.get_image_server()
        if server:
            return server, 200
        else:
            return jsonify({"message": "Servidor no encontrado"}), 404
