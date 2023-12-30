from django.db import models
from User.models import User

class UserAuthBackend:
    """
    Custom authentication bakend.
    Allows users to log in using their username and password
    """

    def authenticate(self,request,username=None,password=None,email=None):
        """
        Overirdes the authenticate method to allow users to log in using their email address or username.
        """
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self,userId):
        """
        Overrides the get_user method to allow to log in using their email address or username
        """
        try:
            return User.objects.get(id=userId)
        except User.DoesNotExist:
            return None