from rest_framework import generics,mixins,permissions,authentication
from .models import Timer
from .serializers import TimerSerializer,RegisterTimeSerialer
from rest_framework.response import Response
from rest_framework.decorators import api_view
import datetime



# Create your views here.

class TimerDetailApi(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.SessionAuthentication]
    queryset = Timer.objects.all()
    serializer_class = TimerSerializer
    lookup_field = 'pk'
    def get(self, request, *args, **kwargs):
        print(args, kwargs)
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request,*args, **kwargs)
        else:
            pass

class TimerApi(generics.CreateAPIView):
    queryset = Timer.objects.all()
    serializer_class = RegisterTimeSerialer
    def perform_create(self, serializer):
        # serializer = RegisterTimeSerialer
        if serializer.is_valid(raise_exception=True):
            print(serializer.validated_data)
            title = serializer.validated_data.get("id")
            activity_time = serializer.validated_data.get("activity_time")or None
            break_time = serializer.validated_data.get("break_time")or None
            take_note = serializer.validated_data.get('take_note')or None
            serializer.save()


class TimerMixinView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView):
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [authentication.SessionAuthentication]
    queryset = Timer.objects.all()
    serializer_class = RegisterTimeSerialer
    lookup_field = 'pk'
    def get(self, request, *args, **kwargs):
        print(args, kwargs)
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request,*args, **kwargs)
        return self.list(request, *args, **kwargs)
 

