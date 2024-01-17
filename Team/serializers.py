from rest_framework import serializers
from .models import Team, TeamDetails, TeamProject

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'
        read_only_fields = ['teamId', 'teamCreatedDate']

class TeamReadSerializer(serializers.ModelSerializer):
     
    class Meta:
        model = Team
        fields = '__all__'
        read_only_fields = ['teamId', 'teamCreatedDate']

class TeamDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamDetails
        fields = '__all__'
        # depth = 1  # This is used to serialize ForeignKey relationships (e.g., TeamDetailsTeamId)

class TeamProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamProject
        fields = '__all__'
        read_only_fields = ['teamProjectId', 'teamProjectCreatedDate']
        # depth = 1  # This is used to serialize ForeignKey relationships (e.g., TeamProjectTeamId, TeamProjectProjectId)

