from drf_spectacular.utils import extend_schema
from rest_framework import  viewsets
from rest_framework import status
from rest_framework.response import Response
from .models import Team, TeamDetails, TeamProject,TeamRole,TeamMembership,TeamMembershipRole,TeamCreateRole
from .serializers import TeamDetailsReadSerializer, TeamSerializer, TeamDetailsSerializer, TeamProjectSerializer,TeamMembershipRoleSerializer,TeamMembershipSerializer,TeamRoleSerializer, TeamCreateRoleSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class TeamDetailsViewSet(viewsets.ModelViewSet):
    queryset = TeamDetails.objects.all()
    serializer_class = TeamDetailsSerializer
    
    @extend_schema(responses=TeamDetailsReadSerializer(many=True))
    def list(self, request, *args, **kwargs):
        queryset = TeamDetails.objects.all()
        serializer = TeamDetailsReadSerializer(queryset,many=True)
        return Response(serializer.data)
        


class TeamProjectViewSet(viewsets.ModelViewSet):
    queryset = TeamProject.objects.all()
    serializer_class = TeamProjectSerializer

class TeamMembershipViewset(viewsets.ModelViewSet):
    queryset = TeamMembership.objects.all()
    serializer_class = TeamMembershipSerializer
    
class TeamRoleViewset(viewsets.ModelViewSet):
    queryset = TeamRole.objects.all()
    serializer_class = TeamRoleSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = TeamCreateRoleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class TeamMembershipRoleViewset(viewsets.ModelViewSet):
    queryset = TeamMembershipRole.objects.all()
    serializer_class = TeamMembershipRoleSerializer
    
    
        
    