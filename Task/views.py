from asyncio.windows_events import NULL
from django.db import connection
from django.http import JsonResponse
from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, authentication, permissions
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import TaskAssignment, Task, SubTask, Priority, Status
from .serializers import TaskAssignmentSerializer, TaskSerializer, SubTaskSerializer, PrioritySerializer, StatusSerializer, PriorityUpdateSerializer,PriorityCreateSerializer

from rest_framework import status
# from .dto import AssignTaskDTO


class AssignTaskView(APIView):
    # @extend_schema(request=AssignTaskDTO)
    def post(self, request):
        try:
            # Extract parameters from the request or any other source
            task_id = request.data.get('taskId')
            assignee_user_id = request.data.get('assigneeUserId')
            assigner_user_id = request.data.get('assignerUserId')

            # Call the stored procedure using a raw SQL query
            with connection.cursor() as cursor:
                cursor.execute("EXEC [dbo].[AssignTask] @TaskID=%s, @AssigneeUserID=%s, @AssignerUserID=%s",
                               [task_id, assignee_user_id, assigner_user_id])

            return JsonResponse({"message": "Task assigned successfully","Task Assignment":{"taskId":task_id,"AssigneeId":assignee_user_id,"AssignerId":assigner_user_id}})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)


class TaskAssignmentsAPIView(APIView):
    @extend_schema(responses=TaskAssignmentSerializer(many=True))
    def get(self, request,pk=None):
        # if request.data.get('taskAssignerUserId'):
        #     task_assignments = TaskAssignment.objects.raw("EXEC GetTaskAssignmentsByAssignerUserId @AssignerUserID=%s",
        #                                                   [request.data.get('taskAssignerUserId')])
        if pk:
            task_assignments = TaskAssignment.objects.raw("EXEC GetTaskAssignmentById @TaskAssignmentId=%s",[pk])
        else:
            task_assignments = TaskAssignment.objects.raw("EXEC GetTaskAssignments")
            
        if not task_assignments:
            return Response({"detail":"not found"})
        else: 
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
        else:
            return PrioritySerializer
    
class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()

    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        return StatusSerializer