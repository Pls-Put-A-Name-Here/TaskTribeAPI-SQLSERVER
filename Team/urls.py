from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeamViewSet, TeamDetailsViewSet, TeamProjectViewSet

router = DefaultRouter()
router.register(r'teams', TeamViewSet)
router.register(r'team-details', TeamDetailsViewSet)
router.register(r'team-projects', TeamProjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
