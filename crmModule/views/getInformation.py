from django.shortcuts import render, redirect, get_object_or_404
from ..models import Sponsor
from ..models import Report
from django.core.files.storage import FileSystemStorage

def getInfo(request):
    sponsors = Sponsor.objects.all()
    return render(request, 'getInformation.html', {
        'sponsors': sponsors
        })

def agreement(request, sponsor_id):

    sponsors = Sponsor.objects.all()
    selected_sponsor = get_object_or_404(Sponsor,pk=sponsor_id)

    if request.method == "POST" and request.FILES.get("uploadedFile"):
        uploadedFile = request.FILES["uploadedFile"]
        selected_sponsor.agreement = uploadedFile
        selected_sponsor.save()


    if selected_sponsor.agreement != None:
        agreement = selected_sponsor.agreement
        return render(request, 'agreement.html',{"sponsors": sponsors, "selected_sponsor": selected_sponsor, "file": agreement})
    else:
        return render(request, 'agreement.html',{"sponsors": sponsors, "selected_sponsor": selected_sponsor, "file": None})
    
    

