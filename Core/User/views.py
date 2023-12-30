"""Views for the user api"""

from rest_framework import  generics, authentication,permissions,viewsets

from Core.User.serializers import UserSerializer,UserDetailsSerializer
from Core.User.models import User

class CreateUserView(generics.CreateAPIView):   
    """Create a new user in the system"""
    serializer_class = UserSerializer
    

class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Retrieve the authenticated user"""
        return self.request.user
    
class UsersView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailsView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserDetailsSerializer
