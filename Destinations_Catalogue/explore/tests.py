from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse

from Destinations_Catalogue.explore.models import Continent, ExploreDestination, Attraction


class ExploreViewTest(TestCase):
    def setUp(self):
        # Create some test data for continents and explore destinations
        continent1 = Continent.objects.create(name="Continent 1")
        continent2 = Continent.objects.create(name="Continent 2")

        # Create mock image files for testing
        image_file1 = SimpleUploadedFile("destination1.jpg", b"file_content_here", content_type="image/jpeg")
        image_file2 = SimpleUploadedFile("destination2.jpg", b"file_content_here", content_type="image/jpeg")

        ExploreDestination.objects.create(name="Destination 1", continent=continent1, image=image_file1)
        ExploreDestination.objects.create(name="Destination 2", continent=continent2, image=image_file2)

    def test_explore_view(self):
        # Send a GET request to the explore view using the reverse URL
        response = self.client.get(reverse('explore'))

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Assert that the correct template is used
        self.assertTemplateUsed(response, 'explore/explore.html')

        # Assert that the response contains the continents in the context
        self.assertIn('continents', response.context)

        # Assert that the response contains the explore destinations in the context
        self.assertIn('explore_destinations', response.context)


class ShowAttractionsViewTest(TestCase):
    def setUp(self):
        # Create a test continent
        self.continent = Continent.objects.create(name="Test Continent")

        # Create a test destination and attractions associated with the continent
        self.destination = ExploreDestination.objects.create(name="Test Destination", continent=self.continent)

        # Create attractions with price and images

        image1 = SimpleUploadedFile(name='attraction_image1.jpg', content=b'', content_type='image/jpeg')
        self.attraction1 = Attraction.objects.create(name="Attraction 1", destination=self.destination, price=10.0,
                                                     image=image1)

        image2 = SimpleUploadedFile(name='attraction_image2.jpg', content=b'', content_type='image/jpeg')
        self.attraction2 = Attraction.objects.create(name="Attraction 2", destination=self.destination, price=15.0,
                                                     image=image2)

    def test_show_attractions_view_with_existing_destination(self):
        # Test behavior when a destination exists

        url = reverse('attraction', kwargs={'pk': self.destination.pk})
        response = self.client.get(url)

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check that the correct template is used
        self.assertTemplateUsed(response, 'explore/attractions.html')

        # Check that the context contains the attractions and destination name
        self.assertIn('attractions', response.context)
        self.assertIn('destination', response.context)

        # Check that the destination name in the context matches the created destination
        self.assertEqual(response.context['destination'], self.destination.name)


