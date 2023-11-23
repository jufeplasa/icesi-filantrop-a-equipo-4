from ..loadFiles import readExcel
from django.shortcuts import render, redirect, get_object_or_404
from ..models import Sponsor, Event, Official, Sponsor_Event
from django.conf import settings
import os

def loadSponsors (request):

    file_path = os.path.join(settings.FILES_EXCEL_DATA_DIR, 'SponsorData.xlsx')

    data = readExcel(file_path)

    for obj_data in data.values():
        obj = Sponsor(
            name=obj_data['name'],
            personType=obj_data['personType'],
            contact_number=obj_data['contact_number'],
            email=obj_data['email'],
            previousColab=obj_data['previousColab']
        )
        obj.save()

    return redirect('sponsor')

def loadEvents (request):

    file_path = os.path.join(settings.FILES_EXCEL_DATA_DIR, 'EventData.xlsx')

    data = readExcel(file_path)

    for obj_data in data.values():
        
        obj = Event(
            name=obj_data['name'],
            event_Type=obj_data['event_type'],
            date=obj_data['date'],
            time=obj_data['time']
        )
        obj.save()

        sponsor=get_object_or_404(Sponsor,name=obj_data['sponsor_name'])

        obj2 = Sponsor_Event(
            event_name=obj,
            Sponsor_id=sponsor,
            participation=obj_data['participation']
        )
        obj2.save()

    return redirect('event')

def loadOfficial (request):

    file_path = os.path.join(settings.FILES_EXCEL_DATA_DIR, 'OfficialData.xlsx')

    data = readExcel(file_path)

    for obj_data in data.values():
        obj = Official(
            ...
        )
        obj.save()

    return redirect('menu')
