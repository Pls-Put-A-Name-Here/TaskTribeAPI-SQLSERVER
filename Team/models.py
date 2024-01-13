from django.db import models
from Core.User.models import User

from django.conf import settings

class Team(models.Model):
    tmIdpk = models.AutoField(primary_key=True)
    tmName = models.CharField(max_length=100, null=True)
    tmLeadUsrIdfk = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,db_column="tmLeadUsrIdfk")
    tmDescription = models.CharField(max_length=100, null=True)
    tmCreatedDate = models.DateField(null=True)
    tmUpdatedDate = models.DateTimeField(auto_now=True)
    tmPrjIdfk = models.ForeignKey('Project.Project', on_delete=models.SET_NULL, null=True,db_column="tmPrjIdfk")

    class Meta:
        managed = False
        db_table = 'tblTeams'



# Create your models here.
class TeamDetails(models.Model):
    teamDetailsId = models.AutoField(primary_key=True,db_column="tmdIdpk")
    teamDetailsTeamId = models.ForeignKey(Team, on_delete=models.CASCADE, null=True,db_column="tmdTmIdfk")
    teamDetailsTeamSize = models.IntegerField(null=True,db_column="tmdTeamSize")
    teamDetailsProjectCount = models.IntegerField(null=True,db_column="tmdProjectCount")
    teamDetailsTeamNotes = models.TextField(null=True,db_column="tmdTeamNotes")
    teamDetailsCreatedDate = models.DateField(null=True,db_column="tmdCreatedDate")
    teamDetailsUpdatedDate = models.DateTimeField(auto_now=True,db_column="tmdUpdatedDate")

    class Meta:
        managed = False
        db_table = 'tblTeamDetails'

# class TeamMembership(models.Model):
#     tmbIdpk = models.AutoField(primary_key=True)
#     tmbUsrIdfk = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#     tmbTmIdfk = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)
#     tmbRoleIdfk = models.ForeignKey(UserRole, on_delete=models.SET_NULL, null=True)

#     class Meta:
#         db_table = 'tblTeamMembership'


class TeamProject(models.Model):
    teamProjectId = models.AutoField(primary_key=True)
    teamProjectTeamId = models.ForeignKey(Team, on_delete=models.CASCADE, null=True,db_column="tmPrjTmIdfk")
    teamProjectProjectId = models.ForeignKey('Project.Project', on_delete=models.CASCADE, null=True,db_column="tmPrjPrjIdfk")
    teamProjectCreatedDate = models.DateField(null=True,db_column="tmPrjCreatedDate")
    teamProjectLastUpdateDate = models.DateTimeField(db_column="tmPrjUpdatedDate")

    class Meta:
        managed = False
        db_table = 'tblTeamProjects'
        
