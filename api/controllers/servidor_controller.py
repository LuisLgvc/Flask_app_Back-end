from flask import jsonify, request
from ..models.servidor import Server

class ServerController:
    
    @classmethod #Endpoint de Prueba http://127.0.0.1:5000/api/servidores METODO POST
    def create_server(cls):
        data = request.json
        new_server = Server(
            name=data.get('name'),
            description=data.get('description')
        )

        server_id = Server.create_server(new_server)

        if server_id:
            return jsonify({"server_id": server_id}), 201
        else:
            return jsonify({"message": "Error al crear el servidor"}), 500

    @classmethod #Endpoint de Prueba http://127.0.0.1:5000/api/servidores METODO GET
    def get_servers(cls):
        servers = Server.get_servers()
        if servers:
            return jsonify([server.serialize() for server in servers]), 200
        else:
            return jsonify({"message": "No se encontraron servidores"}), 404
    
    @classmethod #Endpoint de Prueba http://127.0.0.1:5000/api/servidores/{server_id} METODO GET
    def get_server_by_id(cls, server_id):
        server = Server.get_server_by_id(server_id)
        if server:
            return jsonify(server.serialize()), 200
        else:
            return jsonify({"message": "Servidor no encontrado"}), 404

    @classmethod #Endpoint de Prueba http://127.0.0.1:5000/api/servidores/{server_id} METODO PUT
    def update_server(cls, server_id):
        data = request.json
        if Server.update_server(server_id, data):
            return jsonify({"message": "Servidor actualizado exitosamente"}), 200
        else:
            return jsonify({"message": "Error al actualizar el servidor"}), 500

    @classmethod #Endpoint de Prueba http://127.0.0.1:5000/api/servidores/{server_id} METODO DELETE
    def delete_server(cls, server_id):
        if Server.delete_server(server_id):
            return jsonify({"message": "Servidor eliminado exitosamente"}), 200
        else:
            return jsonify({"message": "Error al eliminar el servidor"}), 500
