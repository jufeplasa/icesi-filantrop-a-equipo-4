from django.forms import ModelForm
from .models import Sponsor

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