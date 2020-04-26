from django.shortcuts import render
from .models import Qanda

# Create your views here.
def qanda(request):
   return render(request, 'qanda.html', {})