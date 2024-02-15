
# consumers.py

import json
from channels.generic.websocket import WebsocketConsumer
from .models import ChatRoom, Message
from django.contrib.auth.models import User

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        # Accept the WebSocket connection
        self.accept()

    def disconnect(self, close_code):
        # Clean up when the WebSocket closes
        pass

    def receive(self, text_data):
        # Receive message from WebSocket
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        user_id = text_data_json['user_id']
        chat_room_id = text_data_json['chat_room_id']

        # Retrieve user and chat room objects
        user = User.objects.get(id=user_id)
        chat_room = ChatRoom.objects.get(id=chat_room_id)

        # Create and save message
        new_message = Message.objects.create(
            sender=user,
            chat_room=chat_room,
            content=message
        )

        # Send message to other clients in the same chat room
        self.send_chat_message(chat_room.id, new_message.content, user.username)

    def send_chat_message(self, chat_room_id, message, sender):
        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message,
            'sender': sender,
            'chat_room_id': chat_room_id
        }))
