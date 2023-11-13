from typing import Any
from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser

# Create your models here.
#class Event_Type(models.Model):
#   TYPE_CHOICES = [
#       ("F", "FLORECIMIENTO"),
#       ("O", "ORGANIZACIONAL")
#   ]
    
#   eventType = models.CharField(
#       choices=TYPE_CHOICES,
#       max_length=1,
#       unique=True,
#       primary_key=True  # Define este campo como la llave primaria
#   )


class Event(models.Model):
    type = [
        ("F","FLORECIMIENTO"),
        ("O","ORGANIZACIONAL")
    ]

    date = models.DateField()
    name = models.CharField(max_length=40, unique=True)
    event_Type = models.CharField(choices=type, max_length=1)
    time = models.TimeField(default='08:00')

    @classmethod
    def create_event(cls, name, date, event_Type, sponsor_name, participation):
        # Crea una nueva instancia de Event y la guarda en la base de datos
        event = cls(name=name, date=date, event_Type=event_Type)
        event.save()

        # Crea una nueva instancia de Sponsor_Event y la asocia con el evento
        sponsor_event = Sponsor_Event(Sponsor_id=sponsor_name, participation=participation, event_name=event)
        sponsor_event.save()

        return event

    
class Sponsor(models.Model):
    type = [
        ("N","NATURAL"),
        ("J","JURIDICA")
    ]
    name = models.CharField(max_length=200, unique=True)
    personType =models.CharField(choices=type, max_length=1)
    contact_number = models.CharField(max_length=200, unique=True)
    email =models.CharField(max_length=200)
    previousColab =models.CharField(max_length=200)
    def __str__(self):
        return self.name


    agreement = models.FileField(upload_to="agreements/", null=True, blank=True)

class Sponsor_Event (models.Model):
    event_name =models.ForeignKey(Event, on_delete=models.CASCADE)
    Sponsor_id =models.ForeignKey(Sponsor, on_delete=models.CASCADE)
    participation =models.CharField(max_length=100)


class Official(AbstractUser):
    name =models.CharField(max_length=45, unique=True)
    email =models.CharField(max_length=100)



class Report(models.Model):

    dateTimeOfUpload = models.DateTimeField(auto_now = True)
    uploadedFile = models.FileField(upload_to = "Uploaded Files/", default="pred")
    officiaId = models.ForeignKey(Official, null=True, blank=True, on_delete=models.CASCADE)
    sponsor_id = models.ForeignKey(Sponsor, on_delete=models.CASCADE)
