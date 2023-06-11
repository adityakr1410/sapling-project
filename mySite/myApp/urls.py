
from django.urls import path,include
from .views import *


urlpatterns = [
   path('',home,name='home'),
   path('prn/',prn,name='prn'),
   path('addProject/',addProject,name='addProject'),
   path('allProject/',allProjects,name='allProject'),
   path('viewProject/<int:id>/',viewProject,name='viewProject'),
   path('addPlant/',addPlant,name='addPlant'),
   
]
