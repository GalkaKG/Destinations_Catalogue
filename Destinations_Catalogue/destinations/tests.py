from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, Client
from django.urls import reverse

from Destinations_Catalogue.destinations.forms import DestinationCreateForm
from Destinations_Catalogue.destinations.models import Destination


class DestinationCreateViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.image = SimpleUploadedFile(
            name='test_image.jpg',
            content=b'',
            content_type='image/jpeg'
        )

    def test_destination_create_view(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('create destination')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'destinations/create-destination.html')


class DestinationDetailsViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.destination = Destination.objects.create(
            name='Test Destination',
            location='Test Location',
            description='Test Description',
            creator=self.user,
            image=SimpleUploadedFile(
                name='test_image.jpg',
                content=b'',
                content_type='image/jpeg'
            )
        )


class DestinationEditViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.destination = Destination.objects.create(
            name='Test Destination',
            location='Test Location',
            description='Test Description',
            creator=self.user
        )

    def test_destination_edit_view(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('edit destination', args=[self.destination.pk])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'destinations/edit-destination.html')

        # Assert that the destination object is available in the context
        self.assertEqual(response.context['object'], self.destination)
