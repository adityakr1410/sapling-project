from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(required=True)
    password1 = forms.CharField(required=True)
    password2 = forms.CharField(required=True)
    
    class Meta:
        model = User
        fields = ("username","email","password1","password2")
        
    
    def save(self,commit=True):
        user = super(NewUserForm,self).save(commit=False)
        self.cleaned_data['email']
        if commit:
            user.save()
        return user

