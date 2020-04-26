from django.shortcuts import render
from django.utils import timezone
from .models import Quote

# Create your views here.

def daily_list(request):
    posts = Quote.objects.filter(published_date__lte=timezone.now()).latest('published_date')
    return render(request, 'dailyquote/daily_list.html', {'posts': posts })