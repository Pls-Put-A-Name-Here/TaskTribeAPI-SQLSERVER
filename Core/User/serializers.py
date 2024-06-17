
"""Serializers for the user API view"""

from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import gettext as _

import django_filters
from rest_framework import serializers
from Core.User.models import User,UserRead

class UserSerializer(serializers.ModelSerializer):
    """Serializer for the user object"""

    class Meta:
        model = get_user_model()
        fields = ['id','email','password','userName','firstName','lastName','profileImage']
        extra_kwargs = {'password':{'write_only':True,'min_length':5}}

    def create(self, validated_data):
        """Create and return a user with encrypted password"""
        return get_user_model().objects.create_user(**validated_data)
    
    def update(self,instance, validated_data):
        """Update and return a user with encrypted password"""
        password = validated_data.pop('password',None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()
        
        return user
    

class UserSerializerAll(serializers.ModelSerializer):
    class Meta:
        Model=get_user_model()
        fields='__all__'      
        

class UserDetailsSerializer(serializers.ModelSerializer):
    # Define a custom field for full name
    fullName = serializers.SerializerMethodField(method_name='get_full_name')

    class Meta:
        model = User  # Replace 'User' with your actual model name
        fields = ['id','last_login','email', 'userName', 'firstName', 'otherName', 'lastName', 'dateOfBirth', 'isActive', 'fullName','profileImage']

    def get_full_name(self, obj) -> str:
        
        """Return the full name of the user"""
        # Combine first name, other name, and capitalized last name into a full name
        lastName = obj.lastName.capitalize() if obj.lastName else ''
        return f"{lastName}, {obj.firstName} {obj.otherName} ".strip()
    
class UserReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRead
        fields = '__all__'

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = {
            'isActive': ['exact'],
        }

class ProfileImageSerializer(serializers.Serializer):
    description = serializers.CharField
    image = serializers.FileField