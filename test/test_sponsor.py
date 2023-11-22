import pytest
from django.urls import reverse
from crmModule.models import Sponsor
from django.test import TestCase, Client
from test.factories import sponsorFactory, sponsor2Factory

class SponsorTestCase(TestCase):

    def setUp(self):
        self.client=Client()
        self.firstSponsor = sponsorFactory.create()
        self.secondSponsor = sponsor2Factory.create()

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
        self.assertEqual(Sponsor.objects.filter(name = data['name']).exists(),True)
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
        self.assertEqual(response.status_code,200)

    def test__delete_sponsor(self):
        self.firstSponsor.save()
        self.secondSponsor.save()
        url = reverse('delete_sponsor', args=[1])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual( Sponsor.objects.filter(name='Carvajal').exists(), False)
        self.assertEqual(len(Sponsor.objects.all()),1)

    def test__search_sponsor(self):
        self.firstSponsor.save()
        self.secondSponsor.save()
        url = reverse('sponsor_detail', args=[2])
        response = self.client.get(url)
        expectedHtml= response.context['template']
        self.assertHTMLEqual(expectedHtml,'sponsor_detail.html')
        self.assertEqual(response.context['sponsor'].name,"Manuelita")
        self.assertEqual(response.status_code,200)

    def test__update_sponsor(self):
        self.firstSponsor.save()
        self.secondSponsor.save()
        data:Sponsor = {
        'name' :"Carvajal",
        'personType' : "J",
        'contact_number':"315471353",
        'email' : "CarCalijal@hotmail.com",
        'previousColab' : "True"
        }
        url = reverse('update_sponsor', args=[1])
        response = self.client.post(url, data)
        self.assertEqual(Sponsor.objects.get(name='Carvajal').email,data['email'])
        self.assertEqual(len(Sponsor.objects.all()),2)


    

