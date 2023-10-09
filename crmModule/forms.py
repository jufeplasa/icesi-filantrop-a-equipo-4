from django.forms import ModelForm
from .models import Sponsor
from .models import Event
from .models import Report


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
