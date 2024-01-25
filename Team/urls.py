from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeamViewSet, TeamDetailsViewSet, TeamProjectViewSet,TeamMembershipViewset,TeamRoleViewset,TeamMembershipRoleViewset

router = DefaultRouter()
router.register(r'teams', TeamViewSet)
router.register(r'team-details', TeamDetailsViewSet)
router.register(r'team-projects', TeamProjectViewSet)
router.register(r'team-roles',TeamRoleViewset)
router.register(r'team-memberships',TeamMembershipViewset)
router.register(r'team-membership-roles',TeamMembershipRoleViewset)

urlpatterns = [
    path('', include(router.urls)),
]
