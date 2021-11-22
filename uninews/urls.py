from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('api/', include('api.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('news/', include('news.urls')),
    path('accounts/', include('allauth.urls')),
]
