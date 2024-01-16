from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, ProjectDetailsViewSet, ProjectTeamViewSet, ProjectDetailViewSet,ProjectDetailsAPIView

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
# router.register(r'project-details', ProjectDetailsViewSet)
router.register(r'project-teams', ProjectTeamViewSet)
# api view does the same job as viewset
# router.register(r'project-details2', ProjectDetailViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('project-details/', ProjectDetailsAPIView.as_view()),
    path('project-details/<int:pk>/', ProjectDetailsAPIView.as_view()),
   
]
