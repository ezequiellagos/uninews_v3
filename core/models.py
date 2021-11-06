from django.db import models

# Create your models here.
class SITE_CONFIG(models.Model):
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=200)
    description = models.CharField(max_length=200, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Configuración"
        verbose_name_plural = "Configuraciones"

    def __str__(self):
        return self.name

