from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.


class UserMangager(BaseUserManager):
    """Manager for users"""

    def create_user(self,email,password=None, **extra_fields):
        if not email:
            raise ValueError("You must provide an email address ")
        """Create, save and return a new user"""
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self,email,password):
        """Create save and return a new superuser"""
        user = self.create_user(email,password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

    def get_by_natural_key(self, email):
        return self.get(email=email)

class User(AbstractBaseUser,PermissionsMixin):
    """ User in the system"""

    email = models.EmailField(max_length=255,unique=True,db_column='usrEmail')
    userName = models.CharField(max_length=255,unique=True,db_column='usrName')
    firstName = models.CharField(max_length=255,db_column='usrFirstName')
    otherName = models.CharField(max_length=255,db_column='usrOtherName')
    lastName = models.CharField(max_length=255,db_column='usrLastName')
    dateOfBirth = models.DateField(default='1999-10-01',db_column='usrDoB')
    genderId = models.ForeignKey('User.Gender',db_column='usrGndIdfk',on_delete=models.CASCADE,default='',null=True)
    titleId = models.ForeignKey('User.Title',db_column='usrTltIdfk',on_delete=models.CASCADE,default='',null=True)
    isActive = models.BooleanField(default=True,db_column='usrActive')
    createdDate = models.DateTimeField(auto_now_add=True,db_column='usrCreatedDate')
    lastEditDate = models.DateTimeField(auto_now=True,db_column='usrUpdateDate')
    profileImage = models.URLField(max_length=255,null=True,db_column='usrProfileImage')

    objects = UserMangager()

    USERNAME_FIELD = 'email'

    class Meta:
        managed = False
        db_table = 'tblUsers'



class Gender(models.Model):
    genderId = models.AutoField(db_column='gndIdpk', primary_key=True)  # Field name made lowercase.
    genderName = models.CharField(db_column='gndName', unique=True, max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    genderDescription = models.CharField(db_column='gndDescription', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    genderCreatedDate= models.DateField(db_column='gndCreatedDate', blank=True, null=True)  # Field name made lowercase.
    genderUpdatedDate = models.TextField(db_column='gndUpdatedDate')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'tblGenders'


class UserRead(models.Model):
    userId = models.IntegerField(primary_key=True)
    userName = models.CharField(max_length=255)
    userOtherName = models.CharField(max_length=255, null=True, blank=True)
    userLastName = models.CharField(max_length=255)
    userEmail = models.EmailField()
    userDateOfBirth = models.DateField()
    userIsActive = models.BooleanField()
    userTitle = models.CharField(max_length=50, null=True, blank=True)
    userGender = models.CharField(max_length=50, null=True, blank=True)
       
class Title(models.Model):
    titleId = models.AutoField(db_column='tltIdpk', primary_key=True)  # Field name made lowercase.
    titleName = models.CharField(db_column='tltName', unique=True, max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    titleShortName = models.CharField(db_column='tltShtName', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    titleDescription = models.CharField(db_column='tltDescription', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    titleCreatedDate = models.DateField(db_column='tltCreatedDate', blank=True, null=True)  # Field name made lowercase.
    titleUpdatedDate = models.TextField(db_column='tltUpdatedDate')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'tblTitles'