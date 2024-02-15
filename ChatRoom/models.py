# models.py

from django.db import models
from Core.User.models import User

class ChatRoom(models.Model):
    name = models.CharField(max_length=100)

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    chat_room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
