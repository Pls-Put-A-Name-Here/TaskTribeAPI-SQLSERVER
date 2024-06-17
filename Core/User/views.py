"""Views for the user api"""

from django.shortcuts import get_object_or_404
from rest_framework import  generics, authentication,permissions,viewsets

from Core.User.serializers import ProfileImageSerializer, UserSerializer,UserDetailsSerializer,UserReadSerializer, UserSerializerAll
from Core.User.models import User,UserRead
from rest_framework.views import APIView
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from django.db import connection
from drf_spectacular.utils import extend_schema
from utils import store_image

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


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@extend_schema(responses=UserDetailsSerializer,request=ProfileImageSerializer)
def ProfileImageView(request):
    if 'description' not in request.data or 'image' not in request.FILES:
        return Response({"error": "Description and image are required fields"}, status=status.HTTP_400_BAD_REQUEST)

    description = request.data['description']
    user = request.user  # Use the authenticated user
    image = request.FILES['image']

    # Assume store_image is a utility function to handle image saving
    image_url = store_image(image)  # You need to implement this function to save the image and return its URL

    user.profileImage = image_url
    user.save()

    serializer = UserDetailsSerializer(user)

    return Response(serializer.data, status=status.HTTP_201_CREATED)