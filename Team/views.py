from rest_framework import viewsets
from .models import Team, TeamDetails, TeamProject
from .serializers import TeamSerializer, TeamDetailsSerializer, TeamProjectSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class TeamDetailsViewSet(viewsets.ModelViewSet):
    queryset = TeamDetails.objects.all()
    serializer_class = TeamDetailsSerializer

class TeamProjectViewSet(viewsets.ModelViewSet):
    queryset = TeamProject.objects.all()
    serializer_class = TeamProjectSerializer
