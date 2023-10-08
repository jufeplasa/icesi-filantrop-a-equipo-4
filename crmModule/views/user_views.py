from django.shortcuts import render, redirect
from ..forms import UserForm
from ..models import Official
from django.contrib.auth import login, logout, authenticate

def signup(request):

    if request.method == 'GET':
        return render(request, 'register_user.html',
                {
                    'form': UserForm
                })
    else:
        if request.POST['password1']==request.POST['password2']:
            try:

                user=Official.objects.create_user(password=request.POST['password1'], name=request.POST['name'], email=request.POST['email'], user=request.POST['user'])
                user.save()
                return redirect('signin')
            
            except:
                return render(request, 'register_user.html',
                              {
                                  'form': UserForm,
                                  "error": 'Username already exist'
                              })
        else:
            return render(request, 'register_user.html',
                              {
                                  'form': UserForm,
                                  "error": 'Password do not match'
                              })
            