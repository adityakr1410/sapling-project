from django.shortcuts import render,redirect
from .forms import NewUserForm
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate

# Create your views here.



def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('view')
    
    form = NewUserForm()
    context = {
        'form':form,
    }
    
    return render(request,'register.html',context)



        