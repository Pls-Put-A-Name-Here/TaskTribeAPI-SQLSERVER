from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Task.views import TaskAssignmentsAPIView,TaskViewSet,SubtaskViewSet,PriorityViewSet,StatusViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'subtasks', SubtaskViewSet)
router.register(r'priorities', PriorityViewSet)
router.register(r'statuses', StatusViewSet)
# router.register(r'task/details',TaskDetailsViewSet)
# router.register(r'task/create',TaskCreateViewSet)
# router.register(r'task/update',TaskUpdateViewSet)
# router.register(r'task-status', StatusViewSet)
# router.register(r'task-priority',PriorityViewSet)
# router.register(r'team',TeamViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('task-assignments/', TaskAssignmentsAPIView.as_view(), name='task-assigment'),
]
