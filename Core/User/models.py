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
    genderId = models.IntegerField(default=0,db_column='usrGndIdfk')
    titleId = models.IntegerField(default=0,db_column='usrTltIdfk')
    isActive = models.BooleanField(default=True,db_column='usrActive')
    createdDate = models.DateTimeField(auto_now_add=True,db_column='usrCreatedDate')
    lastEditDate = models.DateTimeField(auto_now=True,db_column='usrUpdateDate')

    objects = UserMangager()

    USERNAME_FIELD = 'email'

    class Meta:
        managed = True
        db_table = 'tblUsers'


class Gender(models.Model):
    genderId = models.AutoField(primary_key=True)
    genderName = models.CharField(max_length=20, null=True)
    genderDescription = models.CharField(max_length=50, null=True)
    genderCreatedDate = models.DateField(null=True)
    genderUpdatedDate = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tblGenders'
        
class Title(models.Model):
    titleId = models.AutoField(primary_key=True)
    titleName = models.CharField(max_length=50, null=True)
    titleShortName = models.CharField(max_length=5, null=True)
    titleDescription = models.CharField(max_length=25, null=True)
    titleCreatedDate = models.DateField(null=True)
    titleUpdatedDate = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tblTitles'
