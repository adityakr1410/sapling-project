from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from .models import *

import folium 

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
        zoomIn = request.POST.get('zoom')
        owner = request.POST.get('owners')
        cTaker = request.POST.get('cTaker')
        
        proj = project(reg=reg,name=nameOfProject,lat=lat,long=long,zoomIn=zoomIn,owner=owner,careT=cTaker)
        proj.save()
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
    
def allProjects(request):
    
    proj = project.objects.all()
    context = {
        "project":proj
    }
    return render(request,'allProjects.html',context)
    

def viewProject(request,id):
    
    proj = project.objects.get(reg=id)
    
    m = folium.Map(location=[proj.lat,proj.long], zoom_start=proj.zoomIn)
    cord = (proj.lat,proj.long)
    folium.Marker(cord,popup=proj.name).add_to(m)
    
    plnt = plant.objects.filter(parentProject=id)
    context = {
        "plant":plnt,
        "map":m._repr_html_()
    }
    return render(request,'projectView.html',context)
    