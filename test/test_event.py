import pytest
from crmModule.models import Event,Sponsor_Event
from django.urls import reverse
from django.test import TestCase, Client
from test.factories import event1Factory, event2Factory, sponsor2Factory, sponsor3Factory


class EventTestCase(TestCase):

    def setUp(self):
        self.client=Client()
        self.firstEvent=event1Factory.create()
        self.secondEvent=event2Factory.create()
        self.firstSponsor=sponsor2Factory.create()
        self.secondSponsor=sponsor3Factory.create()

    def test_register_event(self):
        self.firstSponsor.save()
        data = {
        'sponsor_name': 'Manuelita',
        'participation': 'Financia',
        'name': 'Almuerzo Manuelita',
        'date': '2023-11-15',
        'time':'13:00',
        'event_Type': 'F',
        }
        response = self.client.post('/event/register/', data)
        self.assertEqual( Event.objects.filter(name=data['name']).exists(), True)
        self.assertEqual( Sponsor_Event.objects.filter(Sponsor_id__name=data['sponsor_name'], participation=data['participation']).exists(), True)

    
    def test_register_manyevents(self):
        self.firstEvent.save()
        self.secondSponsor.save()
        data = {
        'sponsor_name': 'Argos S.A',
        'participation': 'Invitado',
        'name': 'Desayuno Becados Argos',
        'date': '2023-06-15',
        'time':'08:00',
        'event_Type': 'F',
        }
        response = self.client.post('/event/register/', data)
        self.assertEqual( Event.objects.filter(name=data['name']).exists(), True)
        self.assertEqual( Sponsor_Event.objects.filter(Sponsor_id__name=data['sponsor_name'], participation=data['participation']).exists(), True)
        self.assertEqual(len(Event.objects.all()),2)
    
    def test_error_register_event(self):
        self.firstEvent.save()
        self.secondEvent.save()
        self.firstSponsor.save()
        data = {
        'sponsor_name': 'Manuelita',
        'participation': 'Invitado',
        'name': "Almuerzo Manuelita",
        'date': '2023-02-17',
        'time':'13:00',
        'event_Type': 'O',
        }
        response = self.client.post('/event/register/', data)
        self.assertEqual( Sponsor_Event.objects.filter(Sponsor_id__name=data['sponsor_name'], participation=data['participation']).exists(), False)
        self.assertEqual(len(Event.objects.all()),2)

    def test_delete_event(self):
        self.firstEvent.save()
        self.secondEvent.save()
        url = reverse('delete_event', args=[1])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual( Event.objects.filter(name='Almuerzo Manuelita').exists(), False)
        self.assertEqual(len(Event.objects.all()),1)

    def test_search_event(self):
        self.firstEvent.save()
        self.secondEvent.save()
        url = reverse('event_detail', args=[1])
        response = self.client.get(url)
        expectedHtml= response.context['template']
        self.assertHTMLEqual(expectedHtml,'event_detail.html')
        self.assertEqual(response.context['event'].name,"Almuerzo Manuelita")
        self.assertEqual(response.status_code,200)

