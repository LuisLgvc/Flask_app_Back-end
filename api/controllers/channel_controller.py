from flask import jsonify, request
from ..models import Channel

class ChannelController:

    @classmethod #Endpoint de prueba http://127.0.0.1:5000/api/canales METODO POST
    def create_channel(cls):
        data = request.json

        channel = Channel(
            server_id=data.get('server_id'),
            name=data.get('name')
        )

        channel_id = Channel.create_channel(channel)
        response_status = 201 if channel_id else 500

        return jsonify({"channel_id": channel_id}) if channel_id else jsonify({"message": "Error al crear el canal"}), response_status

    @classmethod #Endpoint de prueba http://127.0.0.1:5000/api/canales/1 METODO GET Donde "1" es el ID del servidor del cual deseas obtener los canales.
    def get_channels_by_server(cls, server_id):
        channels = Channel.get_channels_by_server(server_id)
        response_status = 200 if channels else 404

        return jsonify([channel.serialize() for channel in channels]) if channels else jsonify({"message": "No se encontraron canales para el servidor"}), response_status

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
