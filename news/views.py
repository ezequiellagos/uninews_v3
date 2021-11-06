from django.shortcuts import render
from .models import News, University

# Create your views here.
def news_home(request):
    return render(request, 'news/news_home.html')
