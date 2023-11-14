
from django.urls import path, include
from .views import user_views, views, sponsor, event, getInformation
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/', views.home, name='home'),
    path('signup/', user_views.signup, name='signup'),
    path('', user_views.signin,name='signin'),
    path('logout/', user_views.signout,name='signout'),
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
    path('event/l/', event.show_events, name='show_events'),
    path('agreement/<int:agreement_id>/agreements_pdf/<str:pdf_filename>/', getInformation.agreement, name='agreement_pdf'),
    #path('event/register/event/register/', event.register_event,name='register_event'),
    #path('user/',user_views.signup,name='user'),
    #path('event/register/event/register/', event.register_event,name='register_event'),

]

if settings.DEBUG:
    urlpatterns += static(settings.FILES_ROOT, document_root=settings.FILES_ROOT)
