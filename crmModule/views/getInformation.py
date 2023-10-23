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
    selected_sponsor = get_object_or_404(Sponsor, pk=sponsor_id)

    if request.method == "POST" and request.FILES.get("uploadedFile"):
        uploaded_file = request.FILES["uploadedFile"]

        # Crear un nuevo objeto Report asociado al Sponsor
        report = Report.objects.create(
            uploadedFile=uploaded_file,
            sponsor_id=selected_sponsor
        )

    # Resto del código para renderizar la plantilla
    latest_report = Report.objects.filter(sponsor_id=selected_sponsor).latest('dateTimeOfUpload') if Report.objects.filter(sponsor_id=selected_sponsor).exists() else None

    return render(request, 'agreement.html', {"sponsors": sponsors, "selected_sponsor": selected_sponsor, "file": latest_report})

    
    

