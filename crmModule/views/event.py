from django.shortcuts import render, redirect, get_object_or_404
from ..forms import EventForm
from ..models import Event


def event(request):
    events = Event.objects.all()
    return render (request, 'event.html',{
        'events':events
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
            return redirect('event')
        except:
            return render(request, 'register_event.html',
                  {
                      'form':EventForm,
                      'error': "Introduce valid data"
                  })

def event_detail(request, event_id):

    if request.method == 'GET':
        event=get_object_or_404(Event,pk=event_id)
        form =EventForm(instance=event)
        return render(request, 'event_detail.html',
                    {
                        'event':event,
                        'form':form
                    })
    else:
       try: 
        event=get_object_or_404(Event,pk=event_id)
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

def delete_event(request, event_id): 
    event=get_object_or_404(Event,pk=event_id)  
    if request.method == 'POST':
        event.delete()
        return redirect('event')
        