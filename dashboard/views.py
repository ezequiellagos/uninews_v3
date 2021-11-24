import os
from django.shortcuts import render
from .decorators import group_required
from os.path import join, dirname
from dotenv import load_dotenv

# Load .env file
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

supported_groups = os.environ.get("SUPPORTED_GROUPS_DASHBOARD").split(',')

@group_required(*supported_groups)
def home(request):
    return render(request, 'dashboard/home.html')

def profile(request):
    return render(request, 'dashboard/profile.html')