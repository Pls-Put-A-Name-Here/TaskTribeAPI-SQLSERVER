from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, authentication, permissions
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import TaskAssignment, Task, SubTask, Priority, Status
from .serializers import TaskAssignmentSerializer, TaskSerializer, SubTaskSerializer, PrioritySerializer, StatusSerializer, PriorityUpdateSerializer,PriorityCreateSerializer

class TaskAssignmentsAPIView(APIView):
    @extend_schema(responses=TaskAssignmentSerializer(many=True))
    def get(self, request):
        task_assignments = TaskAssignment.objects.raw("EXEC GetTaskAssignments")
        serializer = TaskAssignmentSerializer(task_assignments, many=True)
        return Response(serializer.data)

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()

    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        return TaskSerializer

class SubtaskViewSet(viewsets.ModelViewSet):
    queryset = SubTask.objects.all()

    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        return SubTaskSerializer
    
class PriorityViewSet(viewsets.ModelViewSet):
    queryset = Priority.objects.all()

    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PrioritySerializer
        elif self.request.method == 'POST':
            return PriorityCreateSerializer
    
class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()

    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        return StatusSerializer