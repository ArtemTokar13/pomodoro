from django.urls import path, include
from pomodoro_app import views

urlpatterns = [
    path('', views.index, name='index')
]