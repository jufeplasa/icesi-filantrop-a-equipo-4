from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from ..models import Sponsor

# Create your views here.   

def home(request):
    sponsors=Sponsor.objects.all()
    return render (request, 'home.html',{
        'sponsors':sponsors
    })
 

def menu(request):
    return render(request, 'menu.html')



