from django.shortcuts import render
from .decorators import group_required

supported_groups = ['user', 'admin']

@group_required(*supported_groups)
def home(request):
    return render(request, 'dashboard/home.html')
