from django.forms import ModelForm
from .models import Sponsor
from .models import Report

class SponsorForm(ModelForm):
    class Meta:
        model= Sponsor
        fields = ['name', 'personType','contact_number','email','previousColab']