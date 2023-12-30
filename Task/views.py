from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, authentication, permissions
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import TaskAssignment, Task
from .serializers import TaskAssignmentSerializer, TaskSerializer

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
    