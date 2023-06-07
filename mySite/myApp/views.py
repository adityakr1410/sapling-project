from django.shortcuts import render,redirect
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

def addProject(request):
    
    if request.method == 'POST':
        nameOfProject = request.POST.get('name')
        reg = request.POST.get('reg')
        lat = request.POST.get('lat')
        long = request.POST.get('long')
        owner = request.POST.get('owners')
        print(reg)
        print("hello world")
        return redirect('/')    
    
    else:
        user = get_user_model()
        usernames = user.objects.all()
        context = project.objects.all()
        data = {
            "names":context,
            "users":usernames,
        }
        print(data["users"])
        return render(request,'projectFourm.html',data)
    