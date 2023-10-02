from django.forms import ModelForm
from .models import Sponsor
from .models import Event

class SponsorForm(ModelForm):
    class Meta:
        model= Sponsor
        fields = ['name', 'personType','contact_number','email','previousColab']

class EventForm(ModelForm):
    class Meta:
        model= Event
        fields = ['name','date','event_Type']
        #event_Type = forms.ChoiceField(choices=Event_Type.TYPE_CHOICES)
        labels={
            'name':'Nombre', 'date':'Fecha', 'event_Type':'Tipo de Evento'
            }