from django.urls import path
from .views import *
urlpatterns = [
    path('user/', UserApi.as_view(), name='user'),
    path('manager/<int:pk>/', UserManagerApi.as_view(), name='manager' ),
]