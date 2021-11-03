from django.db import models

# Create your models here.
class SITE_CONFIG(models.Model):
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=200)
    description = models.CharField(max_length=200, default="")
    def __str__(self):
        return self.name

