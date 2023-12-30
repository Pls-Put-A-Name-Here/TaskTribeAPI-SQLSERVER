from django.db import models
from Core.User.models import User

class TaskAssignment(models.Model):
    taskAssignmentId = models.AutoField(primary_key=True)
    taskId = models.IntegerField()
    taskName = models.CharField(max_length=255)
    taskDescription = models.CharField(max_length=255)
    taskStartDate = models.DateField()
    taskDueDate = models.DateField()
    taskCreatedDate = models.DateTimeField()
    taskUpdatedDate = models.DateTimeField()
    taskAssignedDate = models.DateTimeField()
    taskPriority = models.CharField(max_length=255)
    taskStatus = models.CharField(max_length=255)
    taskAssignerUserId = models.IntegerField()
    taskAssigneeUserId = models.IntegerField()
    taskAssigneeName = models.CharField(max_length=255)
    taskAssignerName = models.CharField(max_length=255)

    class Meta:
        managed = False  

class Task(models.Model):
    task = models.AutoField(primary_key=True, db_column='tskIdpk')
    taskName = models.CharField(max_length=100, null=True, db_column='tskName')
    taskAssigneeUserId = models.ForeignKey("User", null=True, on_delete=models.SET_NULL, db_column='tskAssigneeUsrIdfk')
    taskCreatedByUserIdfk = models.ForeignKey("User", null=True, related_name="created_tasks", on_delete=models.SET_NULL, db_column='tskCreatedByUserIdfk')
    taskTeamId = models.ForeignKey("Team", null=True, on_delete=models.SET_NULL, db_column='tskTmIdfk')
    taskProjectId = models.ForeignKey("Project", null=True, on_delete=models.SET_NULL, db_column='tskPrjIdfk')
    taskDescription = models.CharField(max_length=100, null=True, db_column='tskDescription')
    taskStartDate = models.DateField(null=True, db_column='tskStartDate')
    taskDueDate = models.DateField(null=True, db_column='tskDueDate')
    taskPriorityId = models.ForeignKey("Priority", null=True, on_delete=models.SET_NULL, db_column='tskPrtIdfk')
    taskSubtaskId = models.ForeignKey("Status", null=True, on_delete=models.SET_NULL, db_column='tskStaIdfk')
    taskCreatedDate = models.DateField(auto_now_add=True, db_column='tskCreatedDate')
    taskUpdatedDate = models.DateTimeField(auto_now=True, db_column='tskUpdatedDate')

    class Meta:
        db_table = 'tblTasks'


class TaskStatus(models.Model):
    staIdpk = models.AutoField(primary_key=True)
    staName = models.CharField(max_length=20, null=True)
    staDescription = models.CharField(max_length=50, null=True)
    staCreatedDate = models.DateField(null=True)
    staUpdateDate = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tblTaskStatuses'

class TaskStatusHistory(models.Model):
    tshIdpk = models.AutoField(primary_key=True)
    tshTskIdfk = models.ForeignKey('Task', on_delete=models.CASCADE, null=True)
    tskStaIdfk = models.ForeignKey('TaskStatus', on_delete=models.SET_NULL, null=True)
    tshChangeDate = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tblTaskStatusHistory'

class TaskUpdate(models.Model):
    tudIdpk = models.AutoField(primary_key=True)
    tudTskIdfk = models.ForeignKey('Task', on_delete=models.CASCADE, null=True)
    tudUsrfk = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    tkuTitle = models.CharField(max_length=50, null=True)
    tudDetails = models.TextField(null=True)
    tkuChallenges = models.CharField(max_length=150, null=True)
    tudProgress = models.DecimalField(max_digits=6, decimal_places=3, null=True)
    tudCreatedDate = models.DateField(null=True)
    tudUpdatedDate = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tblTaskUpdates'

class SubTask(models.Model):
    stkIdpk = models.AutoField(primary_key=True)
    stkTskIdfk = models.ForeignKey('Task', on_delete=models.CASCADE, null=True)
    stkStaIdfk = models.ForeignKey('TaskStatus', on_delete=models.SET_NULL, null=True)
    stkPrtIdfk = models.ForeignKey('TaskPriority', on_delete=models.SET_NULL, null=True)
    stkActive = models.IntegerField(null=True)
    stkName = models.CharField(max_length=100, null=True)
    stkDescription = models.CharField(max_length=255, null=True)
    stkDueDate = models.DateField(null=True)
    stkCreatedDate = models.DateField(null=True)
    stkUpdatedDate = models.DateTimeField(auto_now=True)
    stkSlug = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = 'tblSubTasks'
