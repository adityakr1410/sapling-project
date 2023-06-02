from django.shortcuts import render
from django.contrib.auth import get_user_model
from .models import *
# Create your views here.


def home(request):
    
    return render(request,'home.html')


def prn(request):
    user = get_user_model()
    context = user.objects.all()
    # context = plant.objects.filter(parentProject=103)
    send = {
        "send":context
    }
    
    return render(request,'home.html',send)

