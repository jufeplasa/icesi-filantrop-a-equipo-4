from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from ..models import Sponsor
from django.contrib.auth.decorators import login_required

# Create your views here.   

@login_required
def home(request):
    sponsors=Sponsor.objects.all()
    return render (request, 'home.html',{
        'sponsors':sponsors
    })
 
@login_required
def menu(request):
    return render(request, 'menu.html')



