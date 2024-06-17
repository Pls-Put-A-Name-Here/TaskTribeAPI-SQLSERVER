"""
TaskTribeAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/

Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Uncomment next two lines to enable admin:
from django.contrib import admin
from drf_spectacular.views import SpectacularAPIView,  SpectacularSwaggerView
from django.urls import include, path

from Core.User import urls as userUrls
from Task import urls as taskUrls
from Team import urls as teamUrls
from Project import urls as projectUrls

urlpatterns = [
    # Uncomment the next line to enable the admin:
    path('admin/', admin.site.urls),
    path('api/v1/schema/',SpectacularAPIView.as_view(),name='api-schema'),
    path('api/v1/docs/', SpectacularSwaggerView.as_view(url_name='api-schema'),name='api-docs'),
    path('api/v1/',include(userUrls)),
    path('api/v1/',include(taskUrls)),
    path('api/v1/',include(teamUrls)),
    path('api/v1/',include(projectUrls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/',include('notifications.urls'))
]
