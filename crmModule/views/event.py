from django.shortcuts import render, redirect, get_object_or_404
from ..forms import EventForm
from ..models import Event


def event(request):
    event = Event.objects.all()
    return render (request, 'event.html',{
        'event':event
    })

def register_event(request):

    if request.method == 'GET':
        #choices = Event_Type.TYPE_CHOICES
        #form = EventForm(choices=choices)
        return render(request, 'register_event.html', 
                {
                    'form': EventForm,
                    'error': "Introduce valid Data"
                })
    else:
        try:
            form = EventForm(request.POST)
            new_event=form.save(commit=False)
            new_event.save()
            print(new_event)
            return redirect('event')
        except:
            return render(request, 'register_event.html',
                  {
                      'form':EventForm,
                      'error': "Introduce valid data"
                  })

def event_detail(request, name):

    if request.method == 'GET':
        event=get_object_or_404(Event,pk=name)
        form =EventForm(instance=event)
        return render(request, 'event_detail.html',
                    {
                        'event':event,
                        'form':form
                    })
    else:
       try: 
        event=get_object_or_404(Event,pk=name)
        form =EventForm(request.POST, instance=event)
        form.save()
        return redirect('event')
       except:
            return render(request, 'event_detail.html',
                    {
                        'event':event,
                        'form':form,
                        'error': "Error updating event"
                    }) 

def delete_sponsor(request, name): 
    event=get_object_or_404(Event,pk=name)  
    if request.method == 'POST':
        event.delete()
        return redirect('event')
        