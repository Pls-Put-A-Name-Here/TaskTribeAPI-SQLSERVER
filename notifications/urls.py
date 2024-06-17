from django.urls import path
from . import views

urlpatterns = [
    path('notifications/', views.notifications_view, name='notifications_view'),
    path('notifications/', views.create_notification, name='create_notification'),
    path('notifications/settings/', views.notifications_settings_view, name='notifications_settings_view'),
    path('notifications/mark-as-read/<int:notification_id>/', views.mark_as_read, name='mark_as_read'),
]
