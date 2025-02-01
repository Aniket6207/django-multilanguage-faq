import unittest
from django.test import TestCase, Client
from django.urls import reverse
from django.core.cache import cache
from rest_framework import status
from ..models import FAQ
from django.conf import settings

class FAQListViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        
        # Dummy Data
        self.faq1 = FAQ.objects.create(question="What is Django?", answer="A web framework")
        self.faq2 = FAQ.objects.create(question="What is Python?", answer="A programming language")

        cache.clear()

    def test_debug(self):
        """
        Test that the debug mode is off
        """
        self.assertEqual(settings.DEBUG,False)

    def test_faq_list_view(self):
        """
        Test if FAQ list view returns a correct list of FAQs with the correct translation.
        """
        url = reverse('faq-list')  
        
        # Test the view with the default 'en' language
        response = self.client.get(url, {'lang': 'en'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(len(data), 2)  
        self.assertEqual(data[0]['question'], "What is Django?")
        self.assertEqual(data[0]['answer'], "A web framework")
        
        # Test the view with a different language hindi
        response = self.client.get(url, {'lang': 'hi'})
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data[0]['question'],"Django क्या है?")  
        self.assertEqual(data[0]['answer'], "एक वेब फ्रेमवर्क") 

    

    