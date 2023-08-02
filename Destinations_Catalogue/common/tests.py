from django.test import TestCase, Client
from django.urls import reverse


class TestIndexView(TestCase):
    def setUp(self):
        self.test_client = Client()

    def test_getProfileIndex_shouldRenderTemplate(self):
        response = self.test_client.get('')
        self.assertTemplateUsed(response, 'common/index.html')


class TestCatalogueView(TestCase):
    def setUp(self):
        self.test_client = Client()

    def test_catalogue_view_shouldRenderTemplate(self):
        response = self.test_client.get(reverse('catalogue'))
        self.assertTemplateUsed(response, 'common/catalogue.html')
