from uuid import uuid1
from django import db
from django.db import models
from rest_framework import serializers
from rest_framework.fields import uuid
from Core.User.models import User
from Project.models import Project
from Team.models import Team

class TaskAssignment(models.Model):
    taskAssignmentId = models.AutoField(primary_key=True)
    taskId = models.IntegerField()
    taskStatusId = models.IntegerField()
    taskPriorityId = models.IntegerField()
    taskName = models.CharField(max_length=255)
    taskDescription = models.CharField(max_length=255)
    taskStartDate = models.DateField()
    taskDueDate = models.DateField()
    taskCreatedDate = models.DateField(auto_now_add=True)
    taskProgress = models.DecimalField(max_digits=6, decimal_places=3)
    # taskUpdatedDate = models.DateTimeField()
    taskAssignedDate = models.DateField()
    taskPriority = models.CharField(max_length=255)
    taskStatus = models.CharField(max_length=255)
    taskAssignerUserId = models.IntegerField()
    taskAssigneeUserId = models.IntegerField()
    taskAssigneeName = models.CharField(max_length=255)
    taskAssignerName = models.CharField(max_length=255)

    class Meta:
        managed = False 
        db_table = 'tblTaskAssignments'
        
class AssignTask(models.Model):
    taskId = models.IntegerField()
    assigneeUserId = models.IntegerField()
    assignerUserId = models.IntegerField()
    
    class Meta:
        managed = False
        
class Priority(models.Model):
    priorityId = models.AutoField(primary_key=True,db_column="prtIdpk")
    priorityName = models.CharField(max_length=20, null=True,db_column="prtName")
    priorityDescription = models.CharField(max_length=50, null=True,db_column="prtDescription")
    priorityCreatedDate = models.DateField(auto_now_add=True,db_column="prtCreatedDate")
    # prtUpdateDate = models.DateField(null=True)

    class Meta:
        managed = False
        db_table = 'tblTaskPriorities'

class Status(models.Model):
    statusId = models.AutoField(primary_key=True,db_column="staIdpk")
    statusName = models.CharField(max_length=20, null=True,db_column="staName")
    statusDescription = models.CharField(max_length=50, null=True,db_column="staDescription")
    statusCreatedDate = models.DateField(auto_now_add=True,db_column="staCreatedDate")
    # staUpdateDate = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False        
        db_table = 'tblTaskStatuses'

class Task(models.Model):
    taskId = models.AutoField(primary_key=True, db_column='tskIdpk')
    taskName = models.CharField(max_length=100, null=True, db_column='tskName')
    taskAssigneeUserId = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, db_column='tskAssigneeUsrIdfk')
    taskCreatedByUserId = models.ForeignKey(User, null=True, related_name="created_tasks", on_delete=models.SET_NULL, db_column='tskCreatedByUserIdfk')
    taskTeamId = models.ForeignKey(Team, null=True, on_delete=models.SET_NULL, db_column='tskTmIdfk')
    taskProjectId = models.ForeignKey(Project, null=True, on_delete=models.SET_NULL, db_column='tskPrjIdfk')
    taskDescription = models.CharField(max_length=100, null=True, db_column='tskDescription')
    taskStartDate = models.DateField(null=True, db_column='tskStartDate')
    taskDueDate = models.DateField(null=True, db_column='tskDueDate')
    taskPriorityId = models.ForeignKey(Priority, null=True, on_delete=models.SET_NULL, db_column='tskPrtIdfk')
    taskStatusId = models.ForeignKey(Status, null=True, on_delete=models.SET_NULL, db_column='tskStaIdfk')
    taskCreatedDate = models.DateField(auto_now_add=True, db_column='tskCreatedDate')
    # taskUpdatedDate = models.DateTimeField(auto_now=True, db_column='tskUpdatedDate')

    class Meta:
        managed = False        
        db_table = 'tblTasks'

class TaskStatusHistory(models.Model):
    tshIdpk = models.AutoField(primary_key=True)
    tshTskIdfk = models.ForeignKey(Task, on_delete=models.CASCADE, null=True)
    tskStaIdfk = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    tshChangeDate = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False        
        db_table = 'tblTaskStatusHistory'

# class TaskUpdate(models.Model):
#     taskUpdateId = models.AutoField(primary_key=True, db_column="tudIdpk")
#     taskUpdateTaskId = models.ForeignKey(Task, on_delete=models.CASCADE, null=True, db_column="tudTskIdfk")
#     taskUpdateTaskAssignmentId = models.ForeignKey(TaskAssignment, on_delete=models.SET_NULL, null=True, db_column="tudTkaIdfk")
#     taskUpdateUserId = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, db_column="tudUsrfk")
#     taskUpdateTitle = models.CharField(max_length=50, null=True, db_column="tudTitle")
#     taskUpdateDetails = models.TextField(null=True, db_column="tudDetails")
#     taskUpdateChallenges = models.CharField(max_length=150, null=True, db_column="tudChallenges")
#     taskUpdateProgress = models.DecimalField(max_digits=6, decimal_places=3, null=True, db_column="tudProgress")
#     taskUpdateCreatedDate = models.DateField(null=False, db_column="tudCreatedDate",auto_now_add=True)
#     # taskUpdateLastUpdateDate = models.DateTimeField(auto_now=True, db_column="tudUpdatedDate")

#     class Meta:
#         managed = False
#         db_table = 'tblTaskUpdates'

class TaskUpdate(models.Model):
    taskUpdateId = models.AutoField(primary_key=True)
    taskUpdateTaskId = models.IntegerField()
    taskUpdateTaskAssignmentId = models.IntegerField()
    taskUpdateUserId = models.IntegerField()
    taskUpdateUserName = models.CharField(max_length=255)
    taskUpdateTitle = models.CharField(max_length=50, null=True)
    taskUpdateDetails = models.TextField(null=True)
    taskUpdateChallenges = models.CharField(max_length=150, null=True)
    taskUpdateProgress = models.DecimalField(max_digits=6, decimal_places=3, null=True)
    taskUpdateDate = models.DateField(null=True)
    
    class Meta:
        managed = False

class SubTask(models.Model):
    stkIdpk = models.AutoField(primary_key=True)
    stkSlug = models.UUIDField(max_length=100,default=uuid1)
    stkTskIdfk = models.ForeignKey(Task, on_delete=models.CASCADE, null=False,db_column="stkTskIdfk")
    stkStaIdfk = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True,db_column="stkStaIdfk")
    stkPrtIdfk = models.ForeignKey(Priority, on_delete=models.SET_NULL, null=True,db_column="stkPrtIdfk")
    stkName = models.CharField(max_length=100, null=True)
    stkDescription = models.CharField(max_length=255, null=False)
    stkActive = models.BooleanField(null=False,default=1)
    stkDueDate = models.DateField(null=False)
    stkCreatedDate = models.DateField(auto_now_add=True)
    # stkUpdatedDate = models.DateTimeField(auto_now=True)
   

    class Meta:
        managed = False
        db_table = 'tblSubTasks'
