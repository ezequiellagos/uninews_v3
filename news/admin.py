from django.contrib import admin
from .models import News, University, Category, Association

class NewsAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at', 'slug')
    list_display = ('title', 'pub_date', 'university', 'active', 'featured', 'visitor_counter')
    list_filter = ('pub_date', 'featured', 'university__alias', 'categories')
    search_fields = ('title', 'summary')
    date_hierarchy = 'pub_date'
    ordering = ('-pub_date',)
    filter_horizontal = ('categories',)

class UniversityAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('name', 'alias', 'active', 'is_public', 'location')
    list_filter = ('active', 'location__region__name')
    search_fields = ('name', 'alias')
    ordering = ('-created_at',)
    autocomplete_fields = ['location']

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('name', 'slug', 'active')
    list_filter = ('active',)
    search_fields = ('name',)
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

class AssociationAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('name', 'alias')
    list_filter = ('created_at',)
    search_fields = ('name', 'alias')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

# Register your models here.
admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(University, UniversityAdmin)
admin.site.register(Association, AssociationAdmin)
