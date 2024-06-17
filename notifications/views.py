from datetime import datetime
from django.shortcuts import render, get_object_or_404
from .models import Notification
from .serializers import NotificationSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def notifications_view(request):
    notifications = Notification.objects.filter(user=request.user).order_by('-date_created')
    serializer = NotificationSerializer(notifications, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_notification(request):
    data = request.data
    data['user'] = request.user.id
    data['date_created'] = datetime.now()
    data['is_read'] = False

    serializer = NotificationSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def notifications_settings_view(request):
    return render(request, 'notifications_settings.html')

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def mark_as_read(request, notification_id):
    notification = get_object_or_404(Notification, id=notification_id)
    notification.is_read = True
    notification.save()
    return Response({'success': 'Notification marked as read'}, status=status.HTTP_200_OK)
