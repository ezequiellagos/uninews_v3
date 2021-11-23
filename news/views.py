from django.shortcuts import render
from .models import News, University, Category, NewsCategory, UniversityAssociation, Association

# Create your views here.
def news_home(request):
    return render(request, 'news/news_home.html')

def news_detail(request, news_id):
    new = News.objects.get(pk=news_id)
    return render(request, 'news/news_detail.html', {'new': new})

def news_list(request):
    news_list = News.objects.all()
    return render(request, 'news/news_list.html', {'news_list': news_list})

def news_list_by_university(request, university_id):
    university = University.objects.get(pk=university_id)
    news_list = university.news_set.all()
    return render(request, 'news/news_list.html', {'news_list': news_list})

def news_list_by_category(request, category_id):
    category = Category.objects.get(pk=category_id)
    news_list = category.news_set.all()
    return render(request, 'news/news_list.html', {'news_list': news_list})

def news_list_by_association(request, association_id):
    association = Association.objects.get(pk=association_id)
    news_list = association.news_set.all()
    return render(request, 'news/news_list.html', {'news_list': news_list})

def news_list_by_university_association(request, university_association_id):
    university_association = UniversityAssociation.objects.get(pk=university_association_id)
    news_list = university_association.news_set.all()
    return render(request, 'news/news_list.html', {'news_list': news_list})

def news_list_by_category_association(request, category_association_id):
    category_association = NewsCategory.objects.get(pk=category_association_id)
    news_list = category_association.news_set.all()
    return render(request, 'news/news_list.html', {'news_list': news_list})

