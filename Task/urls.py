from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Task.views import TaskUpdateView, TaskAssignmentsAPIView,TaskViewSet,SubtaskViewSet,PriorityViewSet,StatusViewSet,TaskAssignmentsByAssigneeAPIView,AssignTaskView,TaskUpdateViewSet,TaskStatusUpdateView

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'subtasks', SubtaskViewSet)
router.register(r'priorities', PriorityViewSet)
router.register(r'statuses', StatusViewSet)
# router.register(r'task/details',TaskDetailsViewSet)
# router.register(r'task/create',TaskCreateViewSet)
# router.register(r'task-updates',TaskUpdateViewSet)
# router.register(r'task-status', StatusViewSet)
# router.register(r'task-priority',PriorityViewSet)
# router.register(r'team',TeamViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('task-assignments/', TaskAssignmentsAPIView.as_view(), name='task-assigment'),
    path('task-assignments/<int:pk>/', TaskAssignmentsAPIView.as_view()),
    path('task-assignments/user/',TaskAssignmentsByAssigneeAPIView.as_view(),name='task-assignment-assignee'),
    # path('task-assignments/',AssignTaskView.as_view(),name='task-assign'),
    path('task-updates/', TaskUpdateView.as_view(), name='task-update'),
    path('task-updates/<int:pk>/', TaskUpdateView.as_view(), name='task-update'),
    path('task/status/update',TaskStatusUpdateView.as_view(),name='task-status-update')
]
