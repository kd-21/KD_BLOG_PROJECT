
from django.contrib import admin
from django.urls import path, include
from . import views
# from django.urls import path
# from . import views

urlpatterns = [
    path('', views.home_chat, name='chat_home'),
    path('<str:room_name>/', views.room, name='room'),
]