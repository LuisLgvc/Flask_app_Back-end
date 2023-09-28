from flask import jsonify, request, session
from ..models.servidor_models import Server

class ServerController:
    
    @classmethod #Endpoint de Prueba http://127.0.0.1:5000/api/servidores METODO POST
    def create_server(cls):
        data = request.json
        new_server = Server(
            nombre=data.get('nombre', None),
            id_usuario=session.get('id_usuario'),
            #descripcion=data.get('descripcion')
        )

        server_id = Server.create_server(new_server)

        if server_id:
            return jsonify({"exito": server_id}), 200
        else:
            return jsonify({"message": "Error al crear el servidor"}), 500

    @classmethod #Endpoint de Prueba http://127.0.0.1:5000/api/servidores METODO GET
    def get_servers(cls, id_usuario):
        #id_usuario = session.get('id_usuario')
        
        servers = Server.get_servers(id_usuario)

        if servers:
            return jsonify(servers), 200
        else:
            return jsonify({"message": "No se encontraron servidores"}), 404


    @classmethod #Endpoint de Prueba http://127.0.0.1:5000/api/servidores/{server_id} METODO GET
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

    # @classmethod #Endpoint de Prueba http://127.0.0.1:5000/api/servidores/{server_id} METODO PUT
    # def update_server(cls, server_id):
    #     data = request.json
    #     if Server.update_server(server_id, data):
    #         return jsonify({"message": "Servidor actualizado exitosamente"}), 200
    #     else:
    #         return jsonify({"message": "Error al actualizar el servidor"}), 500

    # @classmethod #Endpoint de Prueba http://127.0.0.1:5000/api/servidores/{server_id} METODO DELETE
    # def delete_server(cls, server_id):
    #     if Server.delete_server(server_id):
    #         return jsonify({"message": "Servidor eliminado exitosamente"}), 200
    #     else:
    #         return jsonify({"message": "Error al eliminar el servidor"}), 500
