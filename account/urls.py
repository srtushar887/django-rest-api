from django.urls import path, include

from .views import UserRegistrationView, UserLoginView, UserProfileView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='userregister'),
    path('login/', UserLoginView.as_view(), name='userlogin'),
    path('profile/', UserProfileView.as_view(), name='userprofile'),
]
