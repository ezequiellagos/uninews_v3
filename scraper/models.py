from django.db import models
from news.models import University, News
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Scraper(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=200)
    urls = ArrayField(models.URLField(max_length=200), blank=True, null=True)
    description = models.TextField()
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Scraper'
        verbose_name_plural = "Scrapers"

    def __str__(self):
        return self.name

class ScrapersLog(models.Model):
    scraper = models.ForeignKey(Scraper, on_delete=models.PROTECT)
    new = models.ForeignKey(News, on_delete=models.PROTECT, blank=True, null=True)
    message = models.TextField()
    level_messages_choices = (
        ('info', 'Info'),
        ('warning', 'Warning'),
        ('error', 'Error'),
    )
    level_message = models.CharField(max_length=10, choices=level_messages_choices, default='info')
    url_new = models.URLField(max_length=200)    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Scrapers Log'
        verbose_name_plural = "Scrapers Logs"

    def __str__(self):
        return self.message