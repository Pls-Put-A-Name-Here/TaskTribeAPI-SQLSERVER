"""Views for the user api"""

from rest_framework import  generics, authentication,permissions,viewsets

from Core.User.serializers import UserSerializer,UserDetailsSerializer,UserReadSerializer
from Core.User.models import User,UserRead
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import connection
from drf_spectacular.utils import extend_schema

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



class GetUsersAPIView(APIView):
    @extend_schema(responses=UserReadSerializer(many=True))
    def get(self, request, *args, **kwargs):
        try:
            # with connection.cursor() as cursor:
            #     cursor.execute("EXEC [dbo].[GetUsers]")
            #     users_data = cursor.fetchall()
            userDetails = UserRead.objects.raw("EXEC GetUsers")
            # Serialize the data
            serializer = UserReadSerializer(userDetails, many=True)
            # serializer.is_valid()

            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
