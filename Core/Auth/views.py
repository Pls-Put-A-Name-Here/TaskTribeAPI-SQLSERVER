from rest_framework import  generics, authentication,permissions,viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from Core.Auth.serializers import AuthTokenSerializer

# Create your views here.
class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user """
    serializer_class  = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES