from django.shortcuts import render
from .models import Emergency

# Create your views here.
def emergency(request):
   return render(request, 'emergency/emergency_app.html', {})