from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta, datetime
from .models import Motorcycle
from .forms import CreateNewMotorcycle

# This file contains unit tests for views in the Garage app.
# I wrote test methods that test the different properties of views.py.

class MotorcycleListViewTestCase(TestCase):
    # This method runs before each test method to set up some initial data
    def setUp(self):
        self.client = Client()
        self.motorcycle1 = Motorcycle.objects.create(
            motorcycle_text='Test motorcycle 1',
            motorcycle_description='This is a test motorcycle 1',
            motorcycle_brand='Brand 1',
            pub_date=timezone.now(),
        )
        self.motorcycle2 = Motorcycle.objects.create(
            motorcycle_text='Test motorcycle 2',
            motorcycle_description='This is a test motorcycle 2',
            motorcycle_brand='Brand 2',
            pub_date=timezone.now(),
        )

    # This method tests the index view that displays a list of all motorcycles
    def test_index_view(self):
        response = self.client.get(reverse('garage:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'garage/index.html')
        self.assertContains(response, 'Test motorcycle 1')
        self.assertContains(response, 'Test motorcycle 2')

    # This method tests the description view that displays the details of a specific motorcycle
    def test_description_view(self):
        response = self.client.get(
            reverse('garage:description', args=(self.motorcycle1.id,))
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'garage/description.html')
        self.assertContains(response, 'Test motorcycle 1')
        self.assertContains(response, 'This is a test motorcycle 1')

    # This method tests the create view that creates a new motorcycle object
    def test_create_view(self):
        form_data = {
            'motorcycle_text': 'Test motorcycle 3',
            'motorcycle_description': 'This is a test motorcycle 3',
            'motorcycle_brand': 'Brand 3',
            'pub_date': timezone.now(),
        }
        response = self.client.post(reverse('garage:create'), data=form_data)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Motorcycle.objects.count(), 3)

    # This method tests the update view that updates an existing motorcycle object
    def test_update_view(self):
        form_data = {
            'motorcycle_text': 'Updated motorcycle',
            'motorcycle_description': 'This is an updated motorcycle',
            'motorcycle_brand': 'Updated brand',
            'pub_date': timezone.now(),
        }
        response = self.client.post(
            reverse('garage:update', args=(self.motorcycle1.id,)), data=form_data
        )
        self.assertEqual(response.status_code, 302)
        updated_motorcycle = Motorcycle.objects.get(id=self.motorcycle1.id)
        self.assertEqual(updated_motorcycle.motorcycle_text, 'Updated motorcycle')
        self.assertEqual(
            updated_motorcycle.motorcycle_description,
            'This is an updated motorcycle',
        )
        self.assertEqual(updated_motorcycle.motorcycle_brand, 'Updated brand')


    def test_delete_view(self):
        response = self.client.post(
            reverse('garage:delete', args=(self.motorcycle1.id,))
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Motorcycle.objects.count(), 1)
