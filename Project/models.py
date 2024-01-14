from django.db import models
from django.conf import settings


class Project(models.Model):
    prjIdpk = models.AutoField(primary_key=True)
    prjName = models.CharField(max_length=100, null=True)
    prjTmIdfk = models.ForeignKey("Team.Team", on_delete=models.SET_NULL, null=True,db_column="prjTmIdfk")
    prjProjectManagerUsrIdfk = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,db_column="prjProjectManagerUsrIdfk")
    prjStartDate = models.DateField(null=True)
    prjEndDate = models.DateField(null=True)
    prjCreatedDate = models.DateField(null=False,auto_now_add=True)
    # prjUpdatedDate = models.DateTimeField(auto_now=True)

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
    prjTmIdpk = models.AutoField(primary_key=True, db_column="prjtIdpk")
    prjTmPrjIdfk = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, db_column="prjtPrjIdfk")
    prjTmTmIdfk = models.ForeignKey("Team.Team", on_delete=models.CASCADE, null=True, db_column="prjtTmIdfk")

    class Meta:
        managed = False
        db_table = 'tblProjectTeams'

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


