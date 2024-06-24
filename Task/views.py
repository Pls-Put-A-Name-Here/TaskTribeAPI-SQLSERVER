from asyncio.windows_events import NULL
from django.db import connection
from django.http import JsonResponse
from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, authentication, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import TaskAssignment, Task, SubTask, Priority, Status, TaskUpdate
from .serializers import AssignTaskSerializer, TaskAssignmentSerializer, TaskSerializer, SubTaskSerializer, \
    PrioritySerializer, StatusSerializer, PriorityUpdateSerializer, PriorityCreateSerializer, TaskUpdateSerializer,TaskStatusUpdateSerializer

from rest_framework import status
from .dto import AssignTaskDTO



class TaskStatusUpdateView(APIView):
    @extend_schema(request=TaskStatusUpdateSerializer, responses=TaskStatusUpdateSerializer)
    def post(self, request):
        task_id = request.data.get('taskId')
        task_status_id = request.data.get('taskStatusId')

        if not task_id or not task_status_id:
            return Response({'error': 'Both taskId and taskStatusId are required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    "EXEC [dbo].[UpdateTaskAssignmentStatus] @TaskID=%s, @TaskStatusID=%s",
                    [task_id, task_status_id]
                )
                result = cursor.fetchone()

                if not result:
                    return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
                
                res_stat, = result
                if res_stat == 1:
                    return Response({"message": "Task status updated successfully"}, status=status.HTTP_200_OK)
                else:
                    return Response({"message": "Task status update failed"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TaskUpdateView(APIView):
    @extend_schema(responses=TaskUpdateSerializer(many=True))
    def get(self, request, pk=None):
        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    "EXEC [dbo].[GetTaskUpdatesById] @taskAssignmentID=%s",
                    [pk]
                )
                results = cursor.fetchall()
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        results_list = []
        for result in results:
            result_dict = {
                'taskUpdateId': result[0],
                'taskUpdateTaskId': result[1],
                'taskUpdateTaskAssignmentId': result[2],
                'taskUpdateUserId': result[3],
                'taskUpdateUserName': result[4],
                'taskUpdateTitle': result[5],
                'taskUpdateDetails': result[6],
                'taskUpdateChallenges': result[7],
                'taskUpdateProgress': result[8],
                'taskUpdateDate': result[9],
            }
            results_list.append(result_dict)
        if not results_list:
            return Response([])
        else:
            # Serialize the results using the custom serializer
            serializer = TaskUpdateSerializer(results_list, many=True)
            return Response(serializer.data)

    def post(self, request):
        user_id = request.data.get('taskUpdateUserId')
        task_assignment_id = request.data.get('taskUpdateTaskAssignmentId')
        update_details = request.data.get('taskUpdateDetails')
        update_title = request.data.get('taskUpdateTitle')
        update_challenges = request.data.get('taskUpdateChallenges')
        update_progress = request.data.get('taskUpdateProgress')

        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    "EXEC [dbo].[MakeTaskUpdate]  @taskUpdateUserID=%s, @taskUpdateTaskAssignmentID=%s, "
                    "@taskUpdateDetails=%s,@taskUpdateTitle=%s,@taskUpdateChallenges=%s, @taskUpdateProgress=%s",
                    [user_id, task_assignment_id, update_details, update_title, update_challenges, update_progress]
                )
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({'success': True}, status=status.HTTP_201_CREATED)


class AssignTaskView(APIView):
    @extend_schema(request=AssignTaskSerializer)
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

            return JsonResponse({"message": "Task assigned successfully",
                                 "Task Assignment": {"taskId": task_id, "AssigneeId": assignee_user_id,
                                                     "AssignerId": assigner_user_id}})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)


class TaskAssignmentsAPIView(APIView):
    @extend_schema(responses=TaskAssignmentSerializer(many=True))
    def get(self, request, pk=None):
        try:
            if pk:
                task_assignments = TaskAssignment.objects.raw("EXEC GetTaskAssignmentsByTaskId @TaskId=%s", [pk])
            else:
                task_assignments = TaskAssignment.objects.raw("EXEC GetTaskAssignments")

            if not task_assignments:
                return Response({"detail": "not found"})

            serializer = TaskAssignmentSerializer(task_assignments, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=500)

    @extend_schema(request=AssignTaskSerializer)
    def post(self, request):
        try:
            task_id = request.data.get('taskId')
            assignee_user_id = request.data.get('assigneeUserId')
            assigner_user_id = request.data.get('assignerUserId')

            with connection.cursor() as cursor:
                cursor.execute("EXEC [dbo].[AssignTask] @TaskID=%s, @AssigneeUserID=%s, @AssignerUserID=%s",
                               [task_id, assignee_user_id, assigner_user_id])

            response_data = {
                "message": "Task assigned successfully",
                "TaskAssignment": {"taskId": task_id, "AssigneeId": assignee_user_id, "AssignerId": assigner_user_id}
            }

            return JsonResponse(response_data, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    def delete(self, request, pk=None):
        try:
            if pk is None:
                return Response({"detail": "not found"}, status=status.HTTP_400_BAD_REQUEST)

            with connection.cursor() as cursor:
                # Call the stored procedure to delete the task assignment
                cursor.execute("EXEC DeleteTaskAssignment @TaskAssignmentId=%s", [pk])

                # Check the execution status of the stored procedure
                if cursor.rowcount == 0:
                    return Response({"detail": "not found"}, status=status.HTTP_404_NOT_FOUND)
                else:
                    return Response({"detail": "deleted"}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @extend_schema(request=AssignTaskSerializer)
    def put(self, request, pk=None):
        try:
            if pk is None:
                return Response({"detail": "not found"}, status=status.HTTP_400_BAD_REQUEST)

            # Extract parameters from the request or any other source
            task_id = request.data.get('taskId')
            assignee_user_id = request.data.get('assigneeUserId')
            assigner_user_id = request.data.get('assignerUserId')

            # Call the stored procedure using a raw SQL query
            with connection.cursor() as cursor:
                cursor.execute(
                    "EXEC [dbo].[UpdateTaskAssignment] @TaskAssignmentID=%s, @TaskID=%s, @AssigneeUserID=%s, @AssignerUserID=%s",
                    [pk, task_id, assignee_user_id, assigner_user_id])

            return JsonResponse({"message": "Task updated successfully",
                                 "Task Assignment": {"taskId": task_id, "AssigneeId": assignee_user_id,
                                                     "AssignerId": assigner_user_id}})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()

    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        return TaskSerializer


class TaskUpdateViewSet(viewsets.ModelViewSet):
    queryset = TaskUpdate.objects.all()

    def get_serializer_class(self):
        return TaskUpdateSerializer


class SubtaskViewSet(viewsets.ModelViewSet):
    queryset = SubTask.objects.all()

    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        return SubTaskSerializer


class PriorityViewSet(viewsets.ModelViewSet):
    queryset = Priority.objects.all()

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PrioritySerializer
        elif self.request.method == 'POST':
            return PriorityCreateSerializer
        else:
            return PrioritySerializer


class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        return StatusSerializer


class TaskAssignmentsByAssigneeAPIView(APIView):
    @extend_schema(responses=TaskAssignmentSerializer(many=True))
    
    
    def get(self, request, id=None):
        try:
            if request.user.id:
                task_assignments = TaskAssignment.objects.raw("EXEC GetTaskAssignmentsByAssigneeUserId @userId=%s", [request.user.id])
            else:
                task_assignments = TaskAssignment.objects.raw("EXEC GetTaskAssignments")

            if not task_assignments:
                return Response({"detail": "not found"})

            serializer = TaskAssignmentSerializer(task_assignments, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=500)