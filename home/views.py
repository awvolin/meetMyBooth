from django.shortcuts import render
from django.http import Http404
#from .models import Computed

from django.utils import timezone

# Create your views here.

def launch(request):
    return render(request, 'home/launch.html', {})
