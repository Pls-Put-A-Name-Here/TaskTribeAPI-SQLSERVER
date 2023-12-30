# from django.db import models

# class ProjectDetails(models.Model):
#     ProjectID = models.IntegerField()
#     ProjectName = models.CharField(max_length=255)
#     TeamName = models.CharField(max_length=255)
#     ProjectManager = models.CharField(max_length=255)
#     ProjectBudget = models.FloatField()
#     ProjectNotes = models.TextField()
#     ProjectStartDate = models.DateField()
#     ProjectEndDate = models.DateField()

#     class Meta:
#         managed = False 

# def execute_stored_procedure():
#     results = ProjectDetails.objects.raw("EXEC GetProjectDetails")
#     return results

# class ProjectTeam(models.Model):
#     prjTeamIdpk = models.AutoField(primary_key=True)
#     prjTeamPrjIdfk = models.ForeignKey('Project', on_delete=models.CASCADE, null=True)
#     prjTeamTmIdfk = models.ForeignKey('Team', on_delete=models.CASCADE, null=True)

#     class Meta:
#         db_table = 'ProjectTeams'

# class ProjectDetail(models.Model):
#     prjdIdpk = models.AutoField(primary_key=True)
#     prjdPrjIdpk = models.ForeignKey('Project', on_delete=models.CASCADE, null=True)
#     prjdProjectBudget = models.DecimalField(max_digits=18, decimal_places=2, null=True)
#     prjdProjectNotes = models.TextField(null=True)
#     prjdCreatedDate = models.DateField(null=True)
#     prjdUpdatedDate = models.DateTimeField(auto_now=True)

#     class Meta:
#         db_table = 'tblProjectDetails'

# class Project(models.Model):
#     prjIdpk = models.AutoField(primary_key=True)
#     prjName = models.CharField(max_length=100, null=True)
#     prjTmIdfk = models.ForeignKey('Team', on_delete=models.SET_NULL, null=True)
#     prjProjectManagerUsrIdfk = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
#     prjStartDate = models.DateField(null=True)
#     prjEndDate = models.DateField(null=True)
#     prjCreatedDate = models.DateField(null=True)
#     prjUpdatedDate = models.DateTimeField(auto_now=True)

#     class Meta:
#         db_table = 'tblProjects'
