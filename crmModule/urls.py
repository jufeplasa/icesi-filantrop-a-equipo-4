from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('philanth/', views.philanth, name='philanth'),
    path('signin/', views.signin,name='signin'),
    path('logout/', views.signout,name='signout'),
    path('menu/', views.menu,name='menu')
]
