
from .views import *
from django.urls import path
from django.contrib.auth import views as authentication_views

urlpatterns = [
    path('register/',register,name='register'),
    path('login/',authentication_views.LoginView.as_view(template_name='login.html'),name='login'),
    
]
