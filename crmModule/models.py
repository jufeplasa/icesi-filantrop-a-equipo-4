from django.db import models

# Create your models here.
class Event_Type(models.Model):
    eventType = models.CharField(max_length=30, unique=True)

class Event(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=40,unique=True )
    event_Type = models.ForeignKey(Event_Type, on_delete=models.CASCADE)


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

class Sponsor_Event (models.Model):
    event_name =models.ForeignKey(Event, on_delete=models.CASCADE)
    Sponsor_id =models.ForeignKey(Sponsor, on_delete=models.CASCADE)
    participation =models.CharField(max_length=100)

class Official(models.Model):
    password =models.CharField(max_length=10)
    name =models.CharField(max_length=45, unique=True)
    email =models.CharField(max_length=100)
    user =models.CharField(max_length=45)

class Report(models.Model):
    upload_date = models.DateField(unique=True)
    description =models.CharField(max_length=1000)
    officiaId = models.ForeignKey(Official, on_delete=models.CASCADE)
    sponsorId = models.ForeignKey(Sponsor, on_delete=models.CASCADE)