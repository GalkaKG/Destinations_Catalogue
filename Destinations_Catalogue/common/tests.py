from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model, login

from Destinations_Catalogue.common.forms import SearchForm
from Destinations_Catalogue.profiles.models import CustomUser, CustomUserManager


class TestIndexView(TestCase):
    def setUp(self):
        self.test_client = Client()

    def test_getProfileIndex_shouldRenderTemplate(self):
        response = self.test_client.get('')
        self.assertTemplateUsed(response, 'common/index.html')

    def test_getProfilesIndex_shouldReturnCorrectContext(self):
        response = self.test_client.get('')
        user = response.context['user']
        # self.assertEqual(user.username, self.custom_user.username)
        form = response.context['form']
        self.assertEqual(form, SearchForm)


class TestCatalogueView(TestCase):
    def setUp(self):
        self.test_client = Client()

    def test_catalogue_view_shouldRenderTemplate(self):
        response = self.test_client.get(reverse('catalogue'))
        self.assertTemplateUsed(response, 'common/catalogue.html')
