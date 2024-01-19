from drf_spectacular.utils import extend_schema
from rest_framework import  viewsets
from rest_framework.response import Response
from .models import Team, TeamDetails, TeamProject
from .serializers import TeamDetailsReadSerializer, TeamSerializer, TeamDetailsSerializer, TeamProjectSerializer

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
