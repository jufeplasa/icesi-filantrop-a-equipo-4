import pytest
from crmModule.models import Sponsor
from django.test import TestCase, Client
from test.factories import sponsorFactory

class SponsorTestCase(TestCase):

    def setUp(self):
        self.client=Client()
        self.firstSponsor = sponsorFactory.create()

    def test_register_sponsor(self):
        data:Sponsor = {
        'name' :"Carvajal",
        'personType' : "J",
        'contact_number':"315471353",
        'email' : "Carv@gmail.com",
        'previousColab' : "True"
        }
        response = self.client.post('/sponsor/register/', data)
        self.assertEqual(Sponsor.objects.filter(name = data['name']).exists(),True)
        self.assertEqual(len(Sponsor.objects.all()),1)
    
    def test_register_manySponsors(self):
        self.firstSponsor.save()
        data:Sponsor = {
        'name' :"Tecnoquimica",
        'personType' : "J",
        'contact_number':"3187952652",
        'email' : "Tquimicas@gmail.com",
        'previousColab' : "True"
        }
        response = self.client.post('/sponsor/register/', data)
        self.assertEqual(len(Sponsor.objects.all()),2)


    def test_error_register_sponsor(self):
        self.firstSponsor.save()
        data:Sponsor = {
        'name' :"Carvajal",
        'personType' : "J",
        'contact_number':"315471353",
        'email' : "Carv@gmail.com",
        'previousColab' : "True"
        }
        response = self.client.post('/sponsor/register/', data)
        self.assertEqual(len(Sponsor.objects.all()),1)

    

