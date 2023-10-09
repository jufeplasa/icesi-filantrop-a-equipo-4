from django.forms import ModelForm
from .models import Sponsor, Event, Official

class SponsorForm(ModelForm):
    class Meta:
        model= Sponsor
        fields = ['name', 'personType','contact_number','email','previousColab']
        labels = {
            'name': 'Nombre',
            'personType': 'Tipo de persona',
            'contact_number': 'Número de contacto',
            'email': 'Correo electrónico',
            'previousColab': '¿La persona ha colaborado antes con icesi?',
        }

class EventForm(ModelForm):
    class Meta:
        model= Event
        fields = ['name','date','event_Type']
        #event_Type = forms.ChoiceField(choices=Event_Type.TYPE_CHOICES)
        labels={
            'name':'Nombre', 'date':'Fecha', 'event_Type':'Tipo de Evento'
            }

class UserForm(ModelForm):
    class Meta:
        model = Official
        fields = ['password1','name','email','user', 'password2']
        labels={
            'password1':'contraseña',
            'name':'nombre', 
            'email':'correo',
            'user':'user',
            'password2':'confirmar',
        }
