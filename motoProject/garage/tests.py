from django.test import TestCase
from django.urls import reverse
from .models import Motorcycle
from django.utils import timezone
from datetime import timedelta

import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'myproject.settings_test'

# This file contains unit tests for the Garage app.
# I wrote test methods that test the different properties and methods of the model.

# MANUAL TESTS

class MotorcycleModelTestCase(TestCase):
    def setUp(self):
        '''The setUp method is called before each test method, and is used to set up any necessary test data. In this example, we create a new Motorcycle object with some test data and store it as an instance variable, self.motorcycle.'''
        self.motorcycle = Motorcycle.objects.create(
            motorcycle_text='Test motorcycle',
            motorcycle_brand='Test brand',
            motorcycle_description='Test description',
            pub_date=timezone.now(),
        )
    
    def test_motorcycle_str(self):
        '''The test_motorcycle_str method checks if the string representation of the motorcycle object is correct. We use the assertEqual method to compare the string representation of the motorcycle object with the expected value.'''
        self.assertEqual(str(self.motorcycle), 'Test motorcycle')

        
    def test_was_published_recently_with_future_date(self):
        '''The test_was_published_recently_with_future_date method checks if the was_published_recently method of the Motorcycle model returns True when the pub_date is in the future. We create a new Motorcycle object with a future pub_date and use the assertTrue method to check if the method returns True.'''
        future_date = timezone.now() + timedelta(days=30)
        future_motorcycle = Motorcycle(pub_date=future_date)
        self.assertTrue(future_motorcycle.was_published_recently())
        
    def test_was_published_recently_with_old_date(self):
        '''The test_was_published_recently_with_old_date method checks if the was_published_recently method of the Motorcycle model returns False when the pub_date is more than one day in the past. We create a new Motorcycle object with an old pub_date and use the assertFalse method to check if the method returns False.'''
        old_date = timezone.now() - timedelta(days=2)
        old_motorcycle = Motorcycle(pub_date=old_date)
        self.assertFalse(old_motorcycle.was_published_recently())
        
    def test_was_published_recently_with_recent_date(self):
        '''The test_was_published_recently_with_recent_date method checks if the was_published_recently method of the Motorcycle model returns True when the pub_date is less than one day in the past. We create a new Motorcycle object with a recent pub_date and use the assertTrue method to check if the method returns True.'''
        recent_date = timezone.now() - timedelta(hours=23)
        recent_motorcycle = Motorcycle(pub_date=recent_date)
        self.assertTrue(recent_motorcycle.was_published_recently())

