from django.db import models
from Core.User.models import User

from django.conf import settings

class Team(models.Model):
    teamId = models.AutoField(primary_key=True,db_column="tmIdpk")
    teamName = models.CharField(max_length=100, null=True,db_column="tmName")
    teamLeadUserId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,db_column="tmLeadUsrIdfk")
    teamDescription = models.CharField(max_length=100, null=True,db_column="tmDescription")
    teamCreatedDate = models.DateField(auto_now_add=True,db_column="tmCreatedDate")
    teamIsActive = models.BinaryField(default=True,null=True,db_column="tmIsActive")
    # teamUpdatedDate = models.DateTimeField(auto_now=True)
    teamProjectId = models.ForeignKey('Project.Project', on_delete=models.SET_NULL, null=True,db_column="tmPrjIdfk")

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
    teamDetailsCreatedDate = models.DateField(null=False,db_column="tmdCreatedDate",auto_now_add=True)
    # teamDetailsUpdatedDate = models.DateTimeField(auto_now=True,db_column="tmdUpdatedDate")

    class Meta:
        managed = False
        db_table = 'tblTeamDetails'


class TeamProject(models.Model):
    teamProjectId = models.AutoField(primary_key=True,db_column="tmPrjIdpk")
    teamProjectTeamId = models.ForeignKey(Team, on_delete=models.CASCADE, null=True,db_column="tmPrjTmIdfk")
    teamProjectProjectId = models.ForeignKey('Project.Project', on_delete=models.CASCADE, null=True,db_column="tmPrjPrjIdfk")
    teamProjectCreatedDate = models.DateField(null=False,db_column="tmPrjCreatedDate",auto_now_add=True)
    # teamProjectLastUpdateDate = models.DateTimeField(db_column="tmPrjUpdatedDate")

    class Meta:
        managed = False
        db_table = 'tblTeamProjects'

class TeamRole(models.Model):
    teamRoleId = models.AutoField(primary_key=True, db_column='tmrIdpk')
    teamRoleName = models.CharField(max_length=100, db_column='tmrName')
    teamRoleShortName = models.CharField(max_length=100, db_column='tmrShtName')
    teamRoleDescription = models.CharField(max_length=255, db_column='tmrDescription')
    teamRoleCreatedDate = models.DateField(default=models.functions.Now(), db_column='tmrCreatedDate')
    teamRoleLastUpdateDate = models.BinaryField(null=True, db_column='tmrUpdatedDate',editable=False)

    class Meta:
        managed = False
        db_table = 'tblTeamRoles'

class TeamCreateRole(models.Model):
    teamRoleId = models.AutoField(primary_key=True, db_column='tmrIdpk')
    teamRoleName = models.CharField(max_length=100, db_column='tmrName')
    teamRoleShortName = models.CharField(max_length=100, db_column='tmrShtName')
    teamRoleDescription = models.CharField(max_length=255, db_column='tmrDescription')
    teamRoleCreatedDate = models.DateField(auto_now_add=True, db_column='tmrCreatedDate')

    class Meta:
        managed = False
        db_table = 'tblTeamRoles'

class TeamMembership(models.Model):
    teamMembershipId = models.AutoField(primary_key=True, db_column='tmbIdpk')
    teamMembershipUserId = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, db_column='tmbUsrIdfk')
    teamMembershipTeamId = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True, db_column='tmbTmIdfk')
    # teamMembershipTeamRoleId = models.ForeignKey(TeamRole, on_delete=models.CASCADE, null=True, blank=True, db_column='tmbTmrIdfk')
    teamMembershipCreatedDate = models.DateField(auto_now_add=True,null=True,db_column="tmbCreatedDate")
    # teamMembershipLastUpdateDate = models.BinaryField(null=True,db_column="tmbUpdatedDate")

    class Meta:
        managed = False
        db_table = 'tblTeamMemberships'

class TeamMembershipRole(models.Model):
    teamMembershipRoleId = models.AutoField(primary_key=True, db_column='tmbRIdpk')
    teamMembershipRoleTeamMembershipId= models.ForeignKey(TeamMembership,on_delete=models.CASCADE, db_column='tmbRTmbIdfk')
    teamMembershipRoleTeamRoleId = models.ForeignKey(TeamRole,db_column='tmbRTmrIdfk',on_delete=models.CASCADE)
    teamMembershipRoleDescription = models.CharField(max_length=255, db_column='tmbRDescription')
    teamMembershipRoleCreatedDate = models.DateField(auto_now_add=True, db_column='tmbRCreatedDate')
    # teamMembershipRoleLastUpdateDate = models.BinaryField(db_column='tmbRUpdatedDate')

    class Meta:
        managed = False
        db_table = 'tblTeamMembershipRoles'
        
# ToDo:  apiviews for teamMembership and roles as well as stored procedures