from django.urls import path
from . import views

urlpatterns = [
    path('qanda_app', views.qanda, name='qanda_app'),
]