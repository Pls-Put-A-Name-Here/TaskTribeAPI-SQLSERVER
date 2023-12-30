"""Serializers for the Auth view"""

from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import gettext as _
import django_filters
from rest_framework import serializers

class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user auth token."""
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False,                   
    )
     

    def validate(self,attrs):
        """Validate and authenticate the user"""
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(
            request = self.context.get('request'),
            username = email,
            password = password
        )
        if not user:
            msg = _('Unable to authenticate with the provided credentials')
            raise serializers.ValidationError(msg,code='authorization')
        
        attrs['user'] = user


        return attrs
