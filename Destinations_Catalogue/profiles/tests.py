from django.test import TestCase

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

from Destinations_Catalogue.profiles.models import ProfileModel



class ProfileIntegrationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.profile = ProfileModel.objects.create(profile_id=self.user.pk)

    def test_profile_create_view(self):
        url = reverse('create_profile')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/create-profile.html')

        data = {
            'username': 'newuser',
            'password1': 'newpassword',
            'password2': 'newpassword'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful creation
        self.assertRedirects(response, reverse('login'))

        # Verify that a new user and profile were created
        self.assertEqual(get_user_model().objects.count(), 2)
        self.assertEqual(ProfileModel.objects.count(), 2)

    def test_profile_edit_view(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('edit_profile')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/edit-profile.html')

        data = {
            'first_name': 'John',
            'last_name': 'Doe'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful update
        self.assertRedirects(response, reverse('details_profile'))

        # Verify that the profile was updated
        self.profile.refresh_from_db()
        self.assertEqual(self.profile.first_name, 'John')
        self.assertEqual(self.profile.last_name, 'Doe')

    def test_profile_delete_view(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('delete_profile')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/delete-profile.html')

        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)  # Redirect after successful delete
        self.assertRedirects(response, reverse('home'))

        # Verify that the user and profile were deleted
        self.assertEqual(get_user_model().objects.count(), 0)
        self.assertEqual(ProfileModel.objects.count(), 0)
