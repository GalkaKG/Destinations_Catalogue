from django.test import TestCase

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

from Destinations_Catalogue.destinations.models import Destination



class DestinationIntegrationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.destination = Destination.objects.create(
            name='Test Destination',
            creator=self.user
        )

    def test_destination_create_view(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('create_destination')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'destinations/create-destination.html')

        data = {
            'name': 'New Destination',
            'description': 'A beautiful place to visit.'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful creation
        self.assertRedirects(response, reverse('catalogue'))

        # Verify that a new destination was created
        self.assertEqual(Destination.objects.count(), 2)

    def test_destination_edit_view(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('edit_destination', args=[self.destination.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'destinations/edit-destination.html')

        data = {
            'name': 'Updated Destination',
            'description': 'An updated description.'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful update
        self.assertRedirects(response, reverse('details_profile'))

        # Verify that the destination was updated
        self.destination.refresh_from_db()
        self.assertEqual(self.destination.name, 'Updated Destination')
        self.assertEqual(self.destination.description, 'An updated description.')

    def test_destination_delete_view(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('delete_destination', args=[self.destination.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'destinations/delete-destination.html')

        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)  # Redirect after successful delete
        self.assertRedirects(response, reverse('details_profile'))

        # Verify that the destination was deleted
        self.assertEqual(Destination.objects.count(), 0)
