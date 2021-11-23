from django.contrib import admin
from .models import News, University, Category, NewsCategory, UniversityAssociation, Association

class NewsAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('title', 'pub_date', 'university', 'active', 'featured', 'visitor_counter')
    list_filter = ('pub_date', 'featured', 'university__alias', 'categories')
    search_fields = ('title', 'summary')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'pub_date'
    ordering = ('-pub_date',)

class UniversityAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('name', 'alias', 'active', 'location')
    list_filter = ('active', 'location__country__region__name')
    search_fields = ('name', 'alias')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('name', 'slug', 'active')
    list_filter = ('active',)
    search_fields = ('name',)
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

class NewsCategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('news', 'category')
    list_filter = ('category__name',)
    search_fields = ('news__title', 'category__name')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

class AssociationAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('name', 'alias')
    list_filter = ('created_at',)
    search_fields = ('name', 'alias')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

class UniversityAssociationAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('university', 'association')
    list_filter = ('association__name',)
    search_fields = ('university__name', 'association__name')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

# Register your models here.
admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(NewsCategory, NewsCategoryAdmin)
admin.site.register(University, UniversityAdmin)
admin.site.register(Association, AssociationAdmin)
admin.site.register(UniversityAssociation, UniversityAssociationAdmin)
