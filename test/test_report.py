import pytest
from crmModule.models import Report
from django.urls import reverse
from django.test import TestCase, Client
from test.factories import sponsorFactory

class ReportTestCase(TestCase):

    def setUp(self):
        self.client=Client()
        self.firstsponsor=sponsorFactory().create()

    # def test_add_report(self):
    #     self.firstsponsor.save()
    #     url = reverse('event_detail', args=[1])
    #     response = self.client.get(url)
