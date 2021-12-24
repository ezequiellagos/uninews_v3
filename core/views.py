from django.shortcuts import render
from news.models import University, Category

# Create your views here.
def home(request):
    universities = University.objects.all()
    categories = Category.objects.all()

    context = {
        'universities': universities,
        'categories': categories
    }
    return render(request, 'core/home.html', context)

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')
