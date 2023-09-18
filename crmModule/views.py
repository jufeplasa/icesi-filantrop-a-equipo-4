from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .forms import SponsorForm
from .models import Sponsor
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
            
def sponsor(request):
    sponsors=Sponsor.objects.all()
    return render (request, 'sponsor.html',{
        'sponsors':sponsors
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
            return render(request,'signin.html', {'form': AuthenticationForm, 'error': 'Username or password is incorrect' })
        else:
            login(request, user)
            return redirect('menu')

def signout(request):
    logout(request)
    return redirect('home')      

def home(request):
    return render(request, 'home.html')

def menu(request):
    return render(request, 'menu.html')

def register_sponsor(request):

    if request.method == 'GET':
         return render(request, 'register_sponsor.html',
                  {
                      'form':SponsorForm
                  })
    else:
        try:
            form = SponsorForm(request.POST)
            new_sponsor=form.save(commit=False)
            new_sponsor.save()
            print(new_sponsor)
            return redirect('sponsor')
        except:
            return render(request, 'register_sponsor.html',
                  {
                      'form':SponsorForm,
                      'error': "Introduce valid data"
                  })

def sponsor_detail(request, sponsor_id):

    if request.method == 'GET':
        sponsor=get_object_or_404(Sponsor,pk=sponsor_id)
        form =SponsorForm(instance=sponsor)
        return render(request, 'sponsor_detail.html',
                    {
                        'sponsor':sponsor,
                        'form':form
                    })
    else:
       try: 
        sponsor=get_object_or_404(Sponsor,pk=sponsor_id)
        form =SponsorForm(request.POST, instance=sponsor)
        form.save()
        return redirect('sponsor')
       except:
            return render(request, 'sponsor_detail.html',
                    {
                        'sponsor':sponsor,
                        'form':form,
                        'error': "Error updating sponsor"
                    }) 

def delete_sponsor(request, sponsor_id): 
    sponsor=get_object_or_404(Sponsor,pk=sponsor_id)  
    if request.method == 'POST':
        sponsor.delete()
        return redirect('sponsor')
        