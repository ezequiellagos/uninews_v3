from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    url_source = models.URLField()
    url_image = models.URLField()
    slug = models.SlugField(max_length=200, unique=True) # Revisar para autocompletado
    active = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    search_title = models.CharField(max_length=200)
    search_summary = models.TextField()
    search_content = models.TextField()
    visitor_counter = models.IntegerField(default=0)
    university = models.ForeignKey('University', on_delete=models.PROTECT)
    categories = models.ManyToManyField('Category', related_name='news', through='NewsCategory')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'
    
    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    active = models.BooleanField(default=True)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.name

class NewsCategory(models.Model):
    news = models.ForeignKey('News', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Categoría de noticia'
        verbose_name_plural = 'Categorías de noticias'
        unique_together = [['news', 'category']]
    
    def __str__(self):
        return self.news.title + ' - ' + self.category.name


class University(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True) # Revisar para autocompletado
    alias = models.CharField(max_length=10)
    active = models.BooleanField(default=True)
    entities = models.ManyToManyField('Entity', related_name='universities', through='UniversityEntity')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Universidad'
        verbose_name_plural = 'Universidades'
    
    def __str__(self):
        return self.name

class Entity(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True) # Revisar para autocompletado
    alias = models.CharField(max_length=10)
    url_web = models.URLField()
    url_image = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Entidad'
        verbose_name_plural = 'Entidades'
    
    def __str__(self):
        return self.name

class UniversityEntity(models.Model):
    university = models.ForeignKey('University', on_delete=models.CASCADE)
    entity = models.ForeignKey('Entity', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Grupo de Universidad'
        verbose_name_plural = 'Grupos de Universidades'
    
    def __str__(self):
        return self.university.name + ' - ' + self.entity.name
