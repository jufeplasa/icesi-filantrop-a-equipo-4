from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse
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
                return render(request, 'login.html')
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
            

def login(request):
     if request.method == 'GET':
        return render(request, 'login.html',
                  {
                      'form': AuthenticationForm
                  })
     else:
        user= authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request,'login.html', {'form': AuthenticationForm, 'error': 'Username or password is incorrect' })
        else:
            return menu()
            

def home(request):
    return render(request, 'home.html')

def menu(request):
    return render(request, 'menu.html')