from rest_framework import serializers
from .models import Team, TeamDetails, TeamProject, TeamMembership, TeamMembershipRole, TeamRole, TeamCreateRole


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


class TeamDetailsReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamDetails
        fields = '__all__'
        depth = 2


class TeamProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamProject
        fields = '__all__'
        read_only_fields = ['teamProjectId', 'teamProjectCreatedDate']
        # depth = 1  # This is used to serialize ForeignKey relationships (e.g., TeamProjectTeamId, TeamProjectProjectId)


class TeamMembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMembership
        fields = '__all__'
        depth = 3
        read_only_fields = ["teamMembershipLastUpdateDate"]


class TeamRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamRole
        fields = '__all__'
        read_only_fields = ["teamRoleLastUpdateDate"]


class TeamCreateRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamCreateRole
        fields = ['teamRoleName', 'teamRoleShortName', 'teamRoleDescription', 'teamRoleCreatedDate']


class TeamMembershipRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMembershipRole
        fields = '__all__'
        read_only_fields = ["teamMembershipRoleLastUpdateDate"]
