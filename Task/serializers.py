from rest_framework import serializers
from django.contrib.auth import get_user_model
from Task.models import TaskAssignment, Task, SubTask, Priority, Status

class TaskAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskAssignment
        fields = "__all__"
        read_only_fields = ['taskAssignmentId']

class TaskSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Task
        fields = "__all__"

class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = "__all__"

class PrioritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Priority
        fields = "__all__"
        
class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = "__all__"
        


class PriorityCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Priority
        fields = ['priorityName', 'priorityDescription']

class PriorityUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Priority
        fields = ['priorityName', 'priorityDescription']

class PriorityDeleteSerializer(serializers.Serializer):
    prtIdpk = serializers.IntegerField()
    
