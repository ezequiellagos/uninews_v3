from django.contrib import admin
from .models import News, University, Category, NewsCategory, UniversityEntity, Entity

# Register your models here.
admin.site.register(News)
admin.site.register(University)
admin.site.register(Category)
admin.site.register(UniversityEntity)
admin.site.register(NewsCategory)
admin.site.register(Entity)
