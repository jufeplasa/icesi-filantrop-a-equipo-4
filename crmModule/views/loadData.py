from ..loadFiles import readExcel
from django.shortcuts import render
from ..models import Sponsor, Event, Official

def loadSponsors (request):
    data = readExcel('../../excelDatos/SponsorData.xlsx')

    for obj_id, obj_data in data.items:
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

    data = readExcel('../../excelDatos/EventData.xlsx')

    for obj_id, obj_data in data.items:
        obj = Event(
            ...
        )
        obj.save

    print("se logro")
    return render(request,'home.html')

def loadOfficial (request):

    data = readExcel('../../excelDatos/OfficialData.xlsx')

    for obj_id, obj_data in data.items:
        obj = Official(
            ...
        )
        obj.save

    print("se logro")
    return render(request,'home.html')
