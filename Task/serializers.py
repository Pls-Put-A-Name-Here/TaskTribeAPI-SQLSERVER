from rest_framework import serializers
from django.contrib.auth import get_user_model
from Task.models import TaskAssignment, Task

class TaskAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskAssignment
        fields = "__all__"
        read_only_fields = ['taskAssignmentId']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
        