from django.urls import path
from . import views

urlpatterns = [
    path('', views.daily_list, name='daily_list'),
]