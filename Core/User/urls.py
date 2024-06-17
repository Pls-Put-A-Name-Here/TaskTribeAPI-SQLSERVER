"""URL mappings for the user API"""

from django.urls import path,include
from rest_framework.routers import DefaultRouter

from Core.User import views as user_views
from Core.Auth import views as auth_views

router = DefaultRouter()
router.register('users',user_views.UsersView)
router.register('userdetails',user_views.UserDetailsView)

urlpatterns = [
    path('create/',user_views.CreateUserView.as_view(),name='create'),
    path('token/',auth_views.CreateTokenView.as_view(),name='token'),
    path('profile/image/',user_views.ProfileImageView,name="profile_image"),
    path('me/',user_views.ManageUserView.as_view(),name="me"),
    path('user-details/', user_views.GetUsersAPIView.as_view(), name='get_users'),
    path('',include(router.urls))

]
