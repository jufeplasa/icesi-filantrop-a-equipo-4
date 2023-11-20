from django.shortcuts import render, redirect, get_object_or_404
from ..forms import SponsorForm
from ..models import Sponsor


def sponsor(request):
    sponsors=Sponsor.objects.all()
    return render (request, 'sponsor.html',{
        'sponsors':sponsors
    })

def register_sponsor(request):

    if request.method == 'GET':
         return render(request, 'register_sponsor.html',
                  {
                      'form':SponsorForm
                  })
    else:
        try:
            form = SponsorForm(request.POST)
            new_sponsor=form.save(commit=False)
            new_sponsor.save()
            return redirect('sponsor')
        except:
            return render(request, 'register_sponsor.html',
                  {
                      'form':SponsorForm,
                      'error': "Introduce valid data"
                  })

def sponsor_detail(request, sponsor_id):

    sponsor=get_object_or_404(Sponsor,pk=sponsor_id)
    return render(request, 'sponsor_detail.html',
        {
            'sponsor':sponsor,
            'template': 'sponsor_detail.html'
        })
       
def update_sponsor(request, sponsor_id):

    if request.method == 'GET':
        sponsor=get_object_or_404(Sponsor,pk=sponsor_id)
        form =SponsorForm(instance=sponsor)
        return render(request, 'update_sponsor.html',
                    {
                        'form':form
                    })
    else:
       try: 
        sponsor=get_object_or_404(Sponsor,pk=sponsor_id)
        form =SponsorForm(request.POST, instance=sponsor)
        form.save()
        return redirect('homereg')
       except:
            return render(request, 'update_sponsor.html',
                    {
                        'form':form,
                        'error': "Error updating sponsor"
                    }) 

def delete_sponsor(request, sponsor_id): 
    sponsor=get_object_or_404(Sponsor,pk=sponsor_id)  
    if request.method == 'POST':
        sponsor.delete()
        return redirect('sponsor')
        