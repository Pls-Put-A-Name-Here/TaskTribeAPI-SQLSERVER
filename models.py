# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS')
    created = models.DateTimeField()
    user = models.OneToOneField('Tblusers', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    object_repr = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')
    action_flag = models.SmallIntegerField()
    change_message = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('Tblusers', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    model = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS')
    session_data = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)


class Tblgenders(models.Model):
    gndidpk = models.AutoField(db_column='gndIdpk', primary_key=True)  # Field name made lowercase.
    gndname = models.CharField(db_column='gndName', unique=True, max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    gnddescription = models.CharField(db_column='gndDescription', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    gndcreateddate = models.DateField(db_column='gndCreatedDate', blank=True, null=True)  # Field name made lowercase.
    gndupdateddate = models.TextField(db_column='gndUpdatedDate')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'tblGenders'


class Tblprojectdetails(models.Model):
    prjdidpk = models.AutoField(db_column='prjdIdpk', primary_key=True)  # Field name made lowercase.
    prjdprjidpk = models.IntegerField(db_column='prjdPrjIdpk', unique=True, blank=True, null=True)  # Field name made lowercase.
    prjdprojectbudget = models.DecimalField(db_column='prjdProjectBudget', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    prjdprojectnotes = models.TextField(db_column='prjdProjectNotes', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prjdcreateddate = models.DateField(db_column='prjdCreatedDate', blank=True, null=True)  # Field name made lowercase.
    prjdupdateddate = models.TextField(db_column='prjdUpdatedDate')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'tblProjectDetails'


class Tblprojectteams(models.Model):
    prjtmidpk = models.AutoField(db_column='prjTmIdpk', primary_key=True)  # Field name made lowercase.
    prjtmprjidfk = models.IntegerField(db_column='prjTmPrjIdfk', blank=True, null=True)  # Field name made lowercase.
    prjtmtmidfk = models.IntegerField(db_column='prjTmTmIdfk', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblProjectTeams'


class Tblprojects(models.Model):
    prjidpk = models.AutoField(db_column='prjIdpk', primary_key=True)  # Field name made lowercase.
    prjname = models.CharField(db_column='prjName', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    prjtmidfk = models.IntegerField(db_column='prjTmIdfk', blank=True, null=True)  # Field name made lowercase.
    prjprojectmanagerusridfk = models.IntegerField(db_column='prjProjectManagerUsrIdfk', blank=True, null=True)  # Field name made lowercase.
    prjstartdate = models.DateField(db_column='prjStartDate', blank=True, null=True)  # Field name made lowercase.
    prjenddate = models.DateField(db_column='prjEndDate', blank=True, null=True)  # Field name made lowercase.
    prjcreateddate = models.DateField(db_column='prjCreatedDate', blank=True, null=True)  # Field name made lowercase.
    prjupdateddate = models.TextField(db_column='prjUpdatedDate', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'tblProjects'


class Tblsubtasks(models.Model):
    stkidpk = models.AutoField(db_column='stkIdpk', primary_key=True)  # Field name made lowercase.
    stktskidfk = models.IntegerField(db_column='stkTskIdfk', blank=True, null=True)  # Field name made lowercase.
    stkstaidfk = models.IntegerField(db_column='stkStaIdfk', blank=True, null=True)  # Field name made lowercase.
    stkprtidfk = models.IntegerField(db_column='stkPrtIdfk', blank=True, null=True)  # Field name made lowercase.
    stkactive = models.IntegerField(db_column='stkActive', blank=True, null=True)  # Field name made lowercase.
    stkname = models.CharField(db_column='stkName', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    stkdescription = models.CharField(db_column='stkDescription', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    stkduedate = models.DateField(db_column='stkDueDate', blank=True, null=True)  # Field name made lowercase.
    stkcreateddate = models.DateField(db_column='stkCreatedDate', blank=True, null=True)  # Field name made lowercase.
    stkupdateddate = models.TextField(db_column='stkUpdatedDate')  # Field name made lowercase. This field type is a guess.
    stkslug = models.CharField(db_column='stkSlug', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblSubTasks'


class Tbltaskassignments(models.Model):
    tkaidpk = models.AutoField(db_column='tkaIdpk', primary_key=True)  # Field name made lowercase.
    tkatskidfk = models.IntegerField(db_column='tkaTskIdfk', blank=True, null=True)  # Field name made lowercase.
    tkaassigneeusridfk = models.IntegerField(db_column='tkaAssigneeUsrIdfk', blank=True, null=True)  # Field name made lowercase.
    tkaassignerusridfk = models.IntegerField(db_column='tkaAssignerUsrIdfk', blank=True, null=True)  # Field name made lowercase.
    tkaassignmentdate = models.DateField(db_column='tkaAssignmentDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblTaskAssignments'


class Tbltaskcomments(models.Model):
    cmtidpk = models.AutoField(db_column='cmtIdpk', primary_key=True)  # Field name made lowercase.
    cmttskidfk = models.IntegerField(db_column='cmtTskIdfk', blank=True, null=True)  # Field name made lowercase.
    cmtusridfk = models.IntegerField(db_column='cmtUsrIdfk', blank=True, null=True)  # Field name made lowercase.
    cmtcomment = models.TextField(db_column='cmtComment', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cmtcreateddate = models.DateField(db_column='cmtCreatedDate', blank=True, null=True)  # Field name made lowercase.
    cmtupdateddate = models.TextField(db_column='cmtUpdatedDate')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'tblTaskComments'


class Tbltaskpriorities(models.Model):
    prtidpk = models.AutoField(db_column='prtIdpk', primary_key=True)  # Field name made lowercase.
    prtname = models.CharField(db_column='prtName', unique=True, max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    prtdescription = models.CharField(db_column='prtDescription', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    prtcreateddate = models.DateField(db_column='prtCreatedDate', blank=True, null=True)  # Field name made lowercase.
    prtupdatedate = models.TextField(db_column='prtUpdateDate')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'tblTaskPriorities'


class Tbltaskpriorityhistory(models.Model):
    tphidpk = models.AutoField(db_column='tphIdpk', primary_key=True)  # Field name made lowercase.
    tphtskidfk = models.IntegerField(db_column='tphTskIdfk', blank=True, null=True)  # Field name made lowercase.
    tphprtidfk = models.IntegerField(db_column='tphPrtIdfk', blank=True, null=True)  # Field name made lowercase.
    tphchangedate = models.TextField(db_column='tphChangeDate')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'tblTaskPriorityHistory'


class Tbltaskstatushistory(models.Model):
    tshidpk = models.AutoField(db_column='tshIdpk', primary_key=True)  # Field name made lowercase.
    tshtskidfk = models.IntegerField(db_column='tshTskIdfk', blank=True, null=True)  # Field name made lowercase.
    tskstaidfk = models.IntegerField(db_column='tskStaIdfk', blank=True, null=True)  # Field name made lowercase.
    tshchangedate = models.TextField(db_column='tshChangeDate')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'tblTaskStatusHistory'


class Tbltaskstatuses(models.Model):
    staidpk = models.AutoField(db_column='staIdpk', primary_key=True)  # Field name made lowercase.
    staname = models.CharField(db_column='staName', unique=True, max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    stadescription = models.CharField(db_column='staDescription', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    stacreateddate = models.DateField(db_column='staCreatedDate', blank=True, null=True)  # Field name made lowercase.
    staupdatedate = models.TextField(db_column='staUpdateDate')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'tblTaskStatuses'


class Tbltaskupdates(models.Model):
    tudidpk = models.AutoField(db_column='tudIdpk', primary_key=True)  # Field name made lowercase.
    tudtskidfk = models.IntegerField(db_column='tudTskIdfk', blank=True, null=True)  # Field name made lowercase.
    tudusrfk = models.IntegerField(db_column='tudUsrfk', blank=True, null=True)  # Field name made lowercase.
    tkutitle = models.CharField(db_column='tkuTitle', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tuddetails = models.TextField(db_column='tudDetails', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    tkuchallenges = models.CharField(db_column='tkuChallenges', max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tudprogress = models.DecimalField(db_column='tudProgress', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    tudcreateddate = models.DateField(db_column='tudCreatedDate', blank=True, null=True)  # Field name made lowercase.
    tudupdateddate = models.TextField(db_column='tudUpdatedDate')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'tblTaskUpdates'


class Tbltasks(models.Model):
    tskidpk = models.AutoField(db_column='tskIdpk', primary_key=True)  # Field name made lowercase.
    tskname = models.CharField(db_column='tskName', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tskassigneeusridfk = models.IntegerField(db_column='tskAssigneeUsrIdfk', blank=True, null=True)  # Field name made lowercase.
    tskcreatedbyuseridfk = models.IntegerField(db_column='tskCreatedByUserIdfk', blank=True, null=True)  # Field name made lowercase.
    tsktmidfk = models.IntegerField(db_column='tskTmIdfk', blank=True, null=True)  # Field name made lowercase.
    tskprjidfk = models.IntegerField(db_column='tskPrjIdfk', blank=True, null=True)  # Field name made lowercase.
    tskdescription = models.CharField(db_column='tskDescription', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tskstartdate = models.DateField(db_column='tskStartDate', blank=True, null=True)  # Field name made lowercase.
    tskduedate = models.DateField(db_column='tskDueDate', blank=True, null=True)  # Field name made lowercase.
    tskprtidfk = models.IntegerField(db_column='tskPrtIdfk', blank=True, null=True)  # Field name made lowercase.
    tskstaidfk = models.IntegerField(db_column='tskStaIdfk', blank=True, null=True)  # Field name made lowercase.
    tskcreateddate = models.DateField(db_column='tskCreatedDate', blank=True, null=True)  # Field name made lowercase.
    tskupdateddate = models.TextField(db_column='tskUpdatedDate')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'tblTasks'


class Tblteamdetails(models.Model):
    tmdidpk = models.AutoField(db_column='tmdIdpk', primary_key=True)  # Field name made lowercase.
    tmdtmidfk = models.IntegerField(db_column='tmdTmIdfk', unique=True, blank=True, null=True)  # Field name made lowercase.
    tmdteamsize = models.IntegerField(db_column='tmdTeamSize', blank=True, null=True)  # Field name made lowercase.
    tmdprojectcount = models.IntegerField(db_column='tmdProjectCount', blank=True, null=True)  # Field name made lowercase.
    tmdteamnotes = models.TextField(db_column='tmdTeamNotes', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    tmdcreateddate = models.DateField(db_column='tmdCreatedDate', blank=True, null=True)  # Field name made lowercase.
    tmdupdateddate = models.TextField(db_column='tmdUpdatedDate')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'tblTeamDetails'


class Tblteammembership(models.Model):
    tmbidpk = models.AutoField(db_column='tmbIdpk', primary_key=True)  # Field name made lowercase.
    tmbusridfk = models.IntegerField(db_column='tmbUsrIdfk', blank=True, null=True)  # Field name made lowercase.
    tmbtmidfk = models.IntegerField(db_column='tmbTmIdfk', blank=True, null=True)  # Field name made lowercase.
    tmbroleidfk = models.IntegerField(db_column='tmbRoleIdfk', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblTeamMembership'


class Tblteamprojects(models.Model):
    tmprjidpk = models.AutoField(db_column='tmPrjIdpk', primary_key=True)  # Field name made lowercase.
    tmprjprjidfk = models.IntegerField(db_column='tmPrJPrjIdfk', blank=True, null=True)  # Field name made lowercase.
    tmprjtmidfk = models.IntegerField(db_column='tmPrJTmIdfk', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblTeamProjects'


class Tblteams(models.Model):
    tmidpk = models.AutoField(db_column='tmIdpk', primary_key=True)  # Field name made lowercase.
    tmname = models.CharField(db_column='tmName', unique=True, max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tmleadusridfk = models.IntegerField(db_column='tmLeadUsrIdfk', blank=True, null=True)  # Field name made lowercase.
    tmdescription = models.CharField(db_column='tmDescription', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tmcreateddate = models.DateField(db_column='tmCreatedDate', blank=True, null=True)  # Field name made lowercase.
    tmupdateddate = models.TextField(db_column='tmUpdatedDate')  # Field name made lowercase. This field type is a guess.
    tmprjidfk = models.IntegerField(db_column='tmPrjIdfk', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblTeams'


class Tbltitles(models.Model):
    tltidpk = models.AutoField(db_column='tltIdpk', primary_key=True)  # Field name made lowercase.
    tltname = models.CharField(db_column='tltName', unique=True, max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tltshtname = models.CharField(db_column='tltShtName', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tltdescription = models.CharField(db_column='tltDescription', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tltcreateddate = models.DateField(db_column='tltCreatedDate', blank=True, null=True)  # Field name made lowercase.
    tltupdateddate = models.TextField(db_column='tltUpdatedDate')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'tblTitles'


class Tbluserroles(models.Model):
    roleidpk = models.AutoField(db_column='RoleIdpk', primary_key=True)  # Field name made lowercase.
    rolename = models.CharField(db_column='RoleName', unique=True, max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    roledescription = models.CharField(db_column='RoleDescription', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblUserRoles'


class Tblusers(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    usremail = models.CharField(db_column='usrEmail', unique=True, max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    usrname = models.CharField(db_column='usrName', unique=True, max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    usrfirstname = models.CharField(db_column='usrFirstName', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    usrothername = models.CharField(db_column='usrOtherName', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    usrlastname = models.CharField(db_column='usrLastName', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    usrdob = models.DateField(db_column='usrDoB')  # Field name made lowercase.
    usrgndidfk = models.IntegerField(db_column='usrGndIdfk')  # Field name made lowercase.
    usrtltidfk = models.IntegerField(db_column='usrTltIdfk')  # Field name made lowercase.
    usractive = models.BooleanField(db_column='usrActive')  # Field name made lowercase.
    usrcreateddate = models.DateTimeField(db_column='usrCreatedDate')  # Field name made lowercase.
    usrupdatedate = models.DateTimeField(db_column='usrUpdateDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblUsers'


class TblusersGroups(models.Model):
    user = models.ForeignKey(Tblusers, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tblUsers_groups'
        unique_together = (('user', 'group'),)


class TblusersUserPermissions(models.Model):
    user = models.ForeignKey(Tblusers, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tblUsers_user_permissions'
        unique_together = (('user', 'permission'),)
