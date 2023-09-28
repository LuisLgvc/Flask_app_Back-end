from ..models.messages_models import Messages

from flask import jsonify, request, session

from datetime import datetime

class MessagesController:
    """Comentario"""

    @classmethod
    def create_message(cls):
        nombre_canal=request.args.get('nombre_canal', None)

        data = request.json

        message = Messages(
            nombre_canal=nombre_canal,
            contenido=data.get('contenido', None),
            id_usuario=session.get('id_usuario'),
        )
        
        Messages.create_message(message)
        response = {"success": "Exito al crear mensaje"}
        return response, 200

    @classmethod
    def get_messages(cls):
        """Get all chanel messages"""
        nombre_canal=request.args.get('nombre_canal', None)
        
        messages = Messages(
            nombre_canal=nombre_canal
        )
        
        result = Messages.get_messages(messages)
        all_messages = []
        if result is not None:
            for message in result:
                all_messages.append(message.formatted_response())
            return all_messages, 200

    @classmethod
    def update_message(cls, id_message):
        data = request.json

        #data['id_message'] = id_message

        message = Messages(**data)
        
        Messages.update_message(id_message, message)
        response = {"success": "Exito al editar mensaje"}
        return response, 200

    @classmethod
    def delete_message(cls, id_message):
        Messages.delete_message(id_message)
        response = {"success": "Exito al borrar mensaje"}
        return response, 200
            