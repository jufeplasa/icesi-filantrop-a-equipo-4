import pytest
from crmModule.models import Official
from django.test import TestCase, Client

class OfficialTestCase(TestCase):

    def firstUser(self):
        data = {
        'name' :"Esteban Quintero",
        'email' : "destebanQ@gmail.com",
        'username':"esteban1",
        'password1' : "1234",
        'password2' : "1234"
        }
        response=self.client.post('/signup/',data)

    def setUp(self):
        self.client=Client()
    
    def test_register_official(self):
        data = {
        'name' :"Diego Ramirez",
        'email' : "diegoR@gmail.com",
        'username':"diego1",
        'password1' : "1234",
        'password2' : "1234"
        }
        response = self.client.post('/signup/', data)
        self.assertEqual(len(Official.objects.all()),1)
        self.assertEqual(response.status_code,302)

    def test_register_manyofficials(self):
        self.firstUser()
        data = {
        'name' :"Diego Ramirez",
        'email' : "diegoR@gmail.com",
        'username':"diego1",
        'password1' : "1234",
        'password2' : "1234"
        }
        response = self.client.post('/signup/', data)
        self.assertEqual(len(Official.objects.all()),2)
        self.assertEqual(response.status_code,302)
    
    def test_error_register_official(self):
        
        data = {
        'name' :"Diego Ramirez",
        'email' : "diegoR@gmail.com",
        'username':"diego1",
        'password1' : "1234",
        'password2' : "1233"
        }
        response = self.client.post('/signup/', data)
        self.assertEqual(len(Official.objects.all()),0)
        self.assertEqual(response.status_code,200)

    def test_error_existOfficial(self):
        self.firstUser()
        data = {
        'name' :"Esteban Quintero",
        'email' : "destebanQ@gmail.com",
        'username':"esteban1",
        'password1' : "1234",
        'password2' : "1234"
        }
        response=self.client.post('/signup/',data)
        with pytest.raises(Exception):
            len(Official.objects.all())
    
    def test_login(self):
        self.firstUser()
        data = {
            'username':"esteban1",
            "password": "1234"
        }
        
        response=self.client.login(username="esteban1", password= "1234")
        response2=self.client.post('',data)
        self.assertEqual(response,True)
        self.assertEqual(response2.status_code,302)


    #def test_error1_login(self):


    #def test_error2_login(self):
