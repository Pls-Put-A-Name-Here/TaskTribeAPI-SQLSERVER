from rest_framework import serializers
from Task.models import TaskAssignment, Task, SubTask, Priority, Status, TaskUpdate


class TaskAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskAssignment
        fields = "__all__"


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

class TaskUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskUpdate
        fields = [
            'taskUpdateId',
            'taskUpdateTaskId',
            'taskUpdateTaskAssignmentId',
            'taskUpdateUserId',
            'taskUpdateUserName',
            'taskUpdateTitle',
            'taskUpdateDetails',
            'taskUpdateChallenges',
            'taskUpdateProgress',
            'taskUpdateDate',
        ]


class AssignTaskSerializer(serializers.Serializer):
    taskId = serializers.IntegerField()
    assignerUserId = serializers.IntegerField()
    assigneeUserId = serializers.IntegerField()

class TaskStatusUpdateSerializer(serializers.Serializer):
    taskId = serializers.IntegerField
    taskStatusId = serializers.IntegerField