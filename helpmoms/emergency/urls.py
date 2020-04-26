from django.urls import path
from . import views

urlpatterns = [
    path('emergency_app', views.emergency, name='emergency_app'),
]