from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from ..models import Sponsor, Report

# Create your views here.

def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html',
                {
                    'form': UserCreationForm    
                })
    else:
        if request.POST['password1']==request.POST['password2']:
            try:
                user=User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                
                user.save()
                return redirect('signin')
            except:
                return render(request, 'signup.html',
                              {
                                  'form': UserCreationForm,
                                  "error": 'Username already exist'
                              })
        else:
            return render(request, 'signup.html',
                              {
                                  'form': UserCreationForm,
                                  "error": 'Password do not match'
                              })
            


def signin(request):
     if request.method == 'GET':
        return render(request, 'signin.html',
                  {
                      'form': AuthenticationForm
                  })
     else:
        user= authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request,'signin.html', {'form': AuthenticationForm, 'error': 'USUARIO O CONTRASEÑA INCORRECTA' })
        else:
            login(request, user)
            return redirect('menu')

def signout(request):
    logout(request)
    return redirect('home')      

def home(request):
    sponsors=Sponsor.objects.all()
    return render (request, 'home.html',{
        'sponsors':sponsors
    })
 

def menu(request):
    return render(request, 'menu.html')



