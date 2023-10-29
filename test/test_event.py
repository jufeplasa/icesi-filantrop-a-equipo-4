import pytest
from crmModule.models import Event,Sponsor_Event
from django.test import TestCase, Client
from test.factories import eventFactory


class EventTestCase(TestCase):

    def setUp(self):
        self.client=Client()
        self.firstEvent=eventFactory.create()

    # def test_register_event(self):
    #     #self.firstEvent.save()
    #     data = {
    #     'name': 'Evento de Ejemplo',
    #     'date': '2023-11-15',
    #     'event_Type': 'F',  # Puedes usar 'F' para FLORECIMIENTO o 'O' para ORGANIZACIONAL
    #     'sponsor_name': 'Sponsor de Prueba',
    #     'participation': 'Patrocinio Platino'
    #     }
    #     response = self.client.post('/event/register/', data)
    #     print(Event.objects.all())
    #     self.assertEqual(len(Event.objects.all()),1)