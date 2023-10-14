from django.shortcuts import render, redirect
from ..forms import UserForm
from ..models import Official
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm


def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html',
                {
                    'form': UserForm
                })
    else:
        if request.POST['password1']==request.POST['password2']:
            try:

                user=Official.objects.create_user(name=request.POST['name'], email=request.POST['email'], username=request.POST['username'],password=request.POST['password1'])
                user.save()
                return redirect('signin')
            
            except:
                return render(request, 'signup.html',
                              {
                                  'form': UserForm,
                                  "error": 'Username already exist'
                              })
        else:
            return render(request, 'signup.html',
                              {
                                  'form': UserForm,
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
            