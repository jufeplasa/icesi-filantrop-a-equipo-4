from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('sponsor/', views.sponsor, name='sponsor'),
    path('signin/', views.signin,name='signin'),
    path('logout/', views.signout,name='signout'),
    path('menu/', views.menu,name='menu'),
    path('sponsor/register/', views.register_sponsor,name='register_sponsor'),
    path('sponsor/<int:sponsor_id>/', views.sponsor_detail,name='sponsor_detail'),
    path('sponsor/<int:sponsor_id>/delete', views.delete_sponsor,name='delete_sponsor'),
]
