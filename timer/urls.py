from xml.etree.ElementInclude import include
from django.urls import path
from .views import TimerApi,TimerMixinView,TimerDetailApi

urlpatterns = [
    path('',TimerApi.as_view()),
    path('detail/<int:pk>',TimerDetailApi.as_view())
    # path('<int:pk>/',TimerMixinView.as_view())
]
