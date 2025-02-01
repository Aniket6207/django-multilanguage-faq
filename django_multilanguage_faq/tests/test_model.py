import unittest
from django.test import TestCase, Client
from django.urls import reverse
from django.core.cache import cache
from rest_framework import status
from ..models import FAQ

class FAQListViewTest(TestCase):
    def setUp(self):
        # Initialize test client
        self.client = Client()
        
        # Add some FAQ objects to the database
        self.faq1 = FAQ.objects.create(question="What is Django?", answer="A web framework")
        self.faq2 = FAQ.objects.create(question="What is Python?", answer="A programming language")
        
        # Cache should be cleared before every test
        cache.clear()

    def test_faq_list_view(self):
        """
        Test if FAQ list view returns a correct list of FAQs with the correct translation.
        """
        url = reverse('faq-list')  # Make sure 'faq-list' is defined in your urls.py
        
        # Test the view with the default 'en' language
        response = self.client.get(url, {'lang': 'en'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Ensure the structure of the response
        data = response.json()
        self.assertEqual(len(data), 2)  # Should return two FAQs
        self.assertEqual(data[0]['question'], "What is Django?")
        self.assertEqual(data[0]['answer'], "A web framework")
        
        # Test the view with a different language, e.g., Spanish
        response = self.client.get(url, {'lang': 'hi'})
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Assuming that you have a translation for these in Spanish
        self.assertEqual(data[0]['question'],"Django क्या है?")  # Spanish translation for 'What is Django?'
        self.assertEqual(data[0]['answer'], "एक वेब फ्रेमवर्क")  # Spanish translation

    