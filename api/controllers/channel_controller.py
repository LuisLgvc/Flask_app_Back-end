from flask import jsonify, request, session
from ..models.channel_models import Channel

class ChannelController:

    @classmethod #Endpoint de prueba http://127.0.0.1:5000/api/canales METODO POST
    def create_channel(cls):
        
        session['nombre_servidor'] = request.args.get('nombre_servidor', None)
        
        data = request.json

        channel = Channel(
            nombre=data.get('nombre', None),
            id_servidor=data.get('id_servidor', None),
            id_mensaje=data.get('id_mensaje', None),
            nombre_servidor=session.get('nombre_servidor', None)
        )      

        channel_id = Channel.create_channel(channel)
        response_status = 201 if channel_id else 500
        

        return jsonify({"channel_id": "Exito"}), response_status

    @classmethod #Endpoint de prueba http://127.0.0.1:5000/api/canales/1 METODO GET Donde "1" es el ID del servidor del cual deseas obtener los canales.
    def get_channels_by_server(cls):
        data = request.args.get('nombre_servidor', None)
        session['nombre_servidor'] = data
        channels = Channel.get_channels_by_server_name(data)
        response_status = 200 if channels else 404
        return channels, response_status





    @classmethod #Endpoint de prueba http://127.0.0.1:5000/api/canales/2 METODO GET Donde "2" es el ID del canal que deseas obtener.
    def get_channel_by_id(cls, channel_id):
        channel = Channel.get_channel_by_id(channel_id)
        response_status = 200 if channel else 404

        return jsonify(channel.serialize()) if channel else jsonify({"message": "Canal no encontrado"}), response_status

    @classmethod #Endpoint de prueba http://127.0.0.1:5000/api/canales/2 METODO PUT
    def update_channel(cls, channel_id):
        data = request.json

        if Channel.update_channel(channel_id, data):
            return jsonify({"message": "Canal actualizado exitosamente"}), 200
        else:
            return jsonify({"message": "Error al actualizar el canal"}), 500

    @classmethod #Endpoint de prueba http://127.0.0.1:5000/api/canales/2 METODO DELETE 
    def delete_channel(cls, channel_id):
        if Channel.delete_channel(channel_id):
            return jsonify({"message": "Canal eliminado exitosamente"}), 200
        else:
            return jsonify({"message": "Error al eliminar el canal"}), 500
