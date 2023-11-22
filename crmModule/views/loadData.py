from ..loadFiles import readExcel
from django.shortcuts import render
from ..models import Sponsor, Event, Official
from django.conf import settings
import os

def loadSponsors (request):

    file_path = os.path.join(settings.FILES_EXCEL_DATA_DIR, 'SponsorData.xlsx')

    data = readExcel(file_path)

    for obj_data in data.values():
        obj = Sponsor(
            name=obj_data['name'],
            person_type=obj_data['personType'],
            contact_number=obj_data['contact_number'],
            email=obj_data['email'],
            previous_colab=obj_data['previousColab']
        )
        obj.save

    print("se logro")
    return render(request,'home.html')

def loadEvents (request):

    file_path = os.path.join(settings.FILES_EXCEL_DATA_DIR, 'EventData.xlsx')

    data = readExcel(file_path)

    for obj_id, obj_data in data.items:
        obj = Event(
            ...
        )
        obj.save

    print("se logro")
    return render(request,'home.html')

def loadOfficial (request):

    file_path = os.path.join(settings.FILES_EXCEL_DATA_DIR, 'OfficialData.xlsx')

    data = readExcel(file_path)

    for obj_id, obj_data in data.items:
        obj = Official(
            ...
        )
        obj.save

    print("se logro")
    return render(request,'home.html')
