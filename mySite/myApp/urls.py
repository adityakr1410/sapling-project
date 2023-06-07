
from django.urls import path,include
from .views import *


urlpatterns = [
   path('',home,name='home'),
   path('prn/',prn,name='prn'),
   path('addProject/',addProject,name='addProject'),
   
]
