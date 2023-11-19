from ..loadFiles import readExcel
from django.shortcuts import render, redirect
from ..models import Sponsor
import json

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
