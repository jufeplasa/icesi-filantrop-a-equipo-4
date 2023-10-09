
from django.urls import path, include
from .views import user_views, views, sponsor, event, getInformation

urlpatterns = [
    path('home/', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('', views.signin,name='signin'),
    path('logout/', views.signout,name='signout'),
    path('menu/', views.menu,name='menu'),
    path('sponsor/', sponsor.sponsor, name='sponsor'),
    path('sponsor/register/', sponsor.register_sponsor,name='register_sponsor'),
    path('sponsor/<int:sponsor_id>/', sponsor.sponsor_detail,name='sponsor_detail'),
    path('sponsor/home',views.home,name='homereg'),
    path('sponsor/<int:sponsor_id>/delete', sponsor.delete_sponsor,name='delete_sponsor'),
    path('agreement/', getInformation.getInfo, name='agreement'),
    path('agreement/<int:sponsor_id>/', getInformation.agreement, name='agreement'),
    path('sponsor/<int:sponsor_id>/update', sponsor.update_sponsor,name='update_sponsor'),
    path('event/', event.event, name='event'),
    path('event/register/', event.register_event,name='register_event'),
    path('event/<int:event_id>/', event.event_detail,name='event_detail'),
    path('event/<int:event_id>/delete', event.delete_event,name='delete_event'),
    path('user/',user_views.signup,name='user'),
   # path('event/register/event/register/', event.register_event,name='register_event'),
]
