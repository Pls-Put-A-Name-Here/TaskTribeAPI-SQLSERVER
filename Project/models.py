from django.db import models
from django.conf import settings


class Project(models.Model):
    projectId = models.AutoField(primary_key=True, db_column="prjIdpk")
    projectName = models.CharField(max_length=100, null=True, db_column="prjName")
    projectTeamId = models.ForeignKey("Team.Team", on_delete=models.SET_NULL, null=True, db_column="prjTmIdfk")
    projectProjectManagerId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, db_column="prjProjectManagerUsrIdfk")
    projectDescription = models.CharField(null=True,db_column="prjDescription",max_length=255)
    projectStartDate = models.DateField(null=True, db_column="prjStartDate")
    projectEndDate = models.DateField(null=True, db_column="prjEndDate")
    projectCreatedDate = models.DateField(null=False, auto_now_add=True, db_column="prjCreatedDate")

    class Meta:
        managed = False
        db_table = 'tblProjects'


class ProjectDetails(models.Model):
    ProjectID = models.AutoField(primary_key=True)
    ProjectName = models.CharField(max_length=255)
    ProjectTeamName = models.CharField(max_length=255)
    ProjectManager = models.CharField(max_length=255)
    ProjectBudget = models.FloatField()
    ProjectNotes = models.TextField()
    ProjectStartDate = models.DateField()
    ProjectEndDate = models.DateField()

    class Meta:
        managed = True
        
    
    # def execute_stored_procedure(self):
    #     results = ProjectDetails.objects.raw("EXEC GetProjectDetails")
    #     return results

class ProjectTeam(models.Model):
    projectTeamId = models.AutoField(primary_key=True, db_column="prjTmIdpk")
    projectTeamProjectId = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, db_column="prjTmPrjIdfk")
    projectTeamTeamId = models.ForeignKey("Team.Team", on_delete=models.CASCADE, null=True, db_column="prjTmTmIdfk")

    class Meta:
        managed = False
        db_table = 'tblProjectTeams'


class ProjectTeamRead(models.Model):
    projectTeamId = models.IntegerField(primary_key=True)
    teamId = models.IntegerField()
    teamName = models.CharField(max_length=100)
    teamDescription = models.CharField(max_length=100, null=True, blank=True)
    teamCreatedDate = models.DateField()
    teamUpdatedDate = models.BinaryField()
    teamIsActive = models.BooleanField()
    teamLeadName = models.CharField(max_length=255)

    class Meta:
        managed = False  # To indicate that this model is not managed by Django


class ProjectDetail(models.Model):
    prjdIdpk = models.AutoField(primary_key=True)
    prjdPrjIdpk = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    prjdProjectBudget = models.DecimalField(max_digits=18, decimal_places=2, null=True)
    prjdProjectNotes = models.TextField(null=True)
    prjdCreatedDate = models.DateField(null=False,auto_now_add=True)
    # prjdUpdatedDate = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'tblProjectDetails'


