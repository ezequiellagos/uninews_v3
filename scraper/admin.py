from django.contrib import admin
from .models import  Scraper, ScrapersLog

class ScraperAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('name', 'university', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name', 'url')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

class ScrapersLogAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    list_display = ('scraper', 'created_at',)
    list_filter = ('created_at',)
    search_fields = ('scraper',)
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

admin.site.register(Scraper, ScraperAdmin)
admin.site.register(ScrapersLog, ScrapersLogAdmin)
