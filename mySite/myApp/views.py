from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from .models import *

import folium 
from folium.plugins import MarkerCluster

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
    
def addPlant(request):
    
    if request.method == 'POST':
        lat_long = request.POST.get('lat_long')
        lat_long = lat_long.split(",")
        proj = project.objects.get(name=request.POST.get('project'))
        reg = request.POST.get('reg')
        projID = proj.reg
        lat = lat_long[0]
        long = lat_long[1]
        lDate = request.POST.get('lstCheck')
        pStatus = request.POST.get('pStatus')
        pType = request.POST.get('type')
        hDetails = request.POST.get('detail')
        
        plnt = plant(plantID=reg,parentProject=projID,
                     lastChecked=lDate,typeDetails=pType,
                     plantStatus=pStatus,healthDetails=hDetails,lat=lat,long=long)
        plnt.save()
        return redirect('/')
    
    else:
        proj = project.objects.all()
        context = {
            "projects":proj
        }
        return render(request,'plantForum.html',context)
    
def allProjects(request):
    
    proj = project.objects.all()
    context = {
        "project":proj
    }
    return render(request,'allProjects.html',context)
    

def viewProject(request,id):
    
    proj = project.objects.get(reg=id)
    plnts = plant.objects.filter(parentProject=id)
    
    m = folium.Map(location=[proj.lat,proj.long], zoom_start=proj.zoomIn)
    
    marker_cluster = MarkerCluster().add_to(m)
    
    for plnt in plnts:
        folium.Marker(
            location=[plnt.lat,plnt.long],
            popup=plnt.typeDetails+"\nas of- "+plnt.lastChecked,
            icon=folium.Icon(color=plnt.plantStatus,prefix=""),
        ).add_to(marker_cluster)
    
    
    
    # lats = [pln.lat for pln in plnts]
    # longs = [pln.long for pln in plnts] 
    
    # FastMarkerCluster(data=list(zip(lats,longs))).add_to(m)
    
    # cord = (proj.lat,proj.long)
    # folium.Marker(cord,popup=proj.name).add_to(m)
    
    plnt = plant.objects.filter(parentProject=id)
    context = {
        "plant":plnt,
        "map":m._repr_html_()
    }
    return render(request,'projectView.html',context)



def viewDashboard(request):
    user = get_user_model()
    usernames = user.objects.all()
    proj = project.objects.all()
    plnt = plant.objects.all()
    
    
    plants = len(plnt)
    projects = len(proj)
    volunteers = len(usernames)
    
    
    context ={
        'plants':plants,
        'projects':projects,
        'volunteers':volunteers,
        'user':usernames,
        'proj':proj
    }
    
    return render(request,'dashboard.html', context)
    