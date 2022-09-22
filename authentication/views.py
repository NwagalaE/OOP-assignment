from crypt import methods
import email
from rest_framework import permissions
from rest_framework import views
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer,RegisterSerializer
from .models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics,mixins,permissions,authentication
# from .serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from . import serializers

# from rest_auth import 
# from requests import request

# Class based view to Get User Details using Token Authentication

# @api_view(['GET', 'POST'])
class UserDetailAPI(generics.RetrieveAPIView):
    authentication_classes = (TokenAuthentication)
    permission_classes = (IsAuthenticated)
    queryset = User.objects.all()
    serializer = UserSerializer
    lookup_field = 'pk'
    def get(self, request, *args, **kwargs):
        print(args, kwargs)
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request,*args, **kwargs)
        else:
            pass
        # return Response(serializer.data)

#Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    def perform_create(self, serializer):
        print(serializer.validated_data)
        title = serializer.validated_data.get("id")
        first_name = serializer.validated_data.get("first_name")
        last_name = serializer.validated_data.get("last_name")
        password = serializer.validated_data.get("password")
        email = serializer.validated_data.get("email")or None
        serializer.save()



class InformationMixinView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        print(args, kwargs)
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request,*args, **kwargs)
        return self.list(request, *args, **kwargs)




class LoginView(views.APIView):
    # This view should be accessible also for unauthenticated users.
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = serializers.LoginSerializer(data=self.request.data,
            context={ 'request': self.request })
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response(None, status=status.HTTP_202_ACCEPTED)


#views for logging existing user

# class MyObtainTokenPairView(TokenObtainPairView):
    # permission_classes = (AllowAny,)
    # serializer_class = MyTokenObtainPairSerializer