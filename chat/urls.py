from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('room1/', views.room1, name='room1'),
    path('room2/', views.room2, name='room2'),
    path('room3/', views.room3, name='room3'),
]
