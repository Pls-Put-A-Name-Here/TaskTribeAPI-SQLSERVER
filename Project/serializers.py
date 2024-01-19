from rest_framework import serializers
from .models import Project,ProjectDetails, ProjectTeam, ProjectDetail, ProjectTeamRead

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

# class ProjectDetailsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProjectDetails
#         fields = '__all__'

class ProjectDetailsSerializer(serializers.Serializer):
    ProjectID = serializers.IntegerField()
    ProjectName = serializers.CharField(max_length=255)
    ProjectTeamName = serializers.CharField(max_length=255)
    ProjectManager = serializers.CharField(max_length=255)
    ProjectBudget = serializers.FloatField()
    ProjectNotes = serializers.CharField()
    ProjectStartDate = serializers.DateField()
    ProjectEndDate = serializers.DateField()


class ProjectTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectTeam
        fields = '__all__'

class ProjectTeamReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectTeamRead
        fields = '__all__'
        
class ProjectDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectDetail
        fields = '__all__'

