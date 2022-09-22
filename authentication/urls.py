from django.urls import path
from .views import UserDetailAPI,RegisterUserAPIView,InformationMixinView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('details/<int:pk>',UserDetailAPI.as_view()),
    path('register',RegisterUserAPIView.as_view()),
    path('details',InformationMixinView.as_view()),
    # path('logout',InformationMixinView.as_view()),
    # path('register',InformationMixinView.as_view()), 
]
