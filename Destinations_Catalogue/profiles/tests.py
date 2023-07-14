from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from Destinations_Catalogue.profiles.models import CustomUser, CustomUserManager
from django.urls import reverse


class LoginViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = get_user_model().objects.create_user(
            username=self.username,
            password=self.password
        )

    def test_login_view(self):
        url = reverse('login')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/login.html')

        # Send POST request with login credentials
        login_data = {
            'username': self.username,
            'password': self.password
        }
        response = self.client.post(url, login_data)

        # Assert that the user is redirected after successful login
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))  # Replace 'home' with the appropriate URL name

        # Verify that the user is logged in
        user = CustomUser.objects.get(username=self.username)
        self.assertTrue(user.is_authenticated)

    def test_login_view_invalid_credentials(self):
        url = reverse('login')
        login_data = {
            'username': 'invalidusername',
            'password': 'invalidpassword'
        }
        response = self.client.post(url, login_data)

        # Assert that the login fails and the user is not redirected
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/login.html')


class ProfileCreateViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.username = 'testuser'
        self.password = 'testpassword'

    def test_profile_create_view(self):
        url = reverse('create profile')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/create-profile.html')


class LogoutViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = get_user_model().objects.create_user(
            username=self.username,
            password=self.password
        )

    def test_logout_view(self):
        # Log in the user
        self.client.login(username=self.username, password=self.password)

        url = reverse('logout')
        response = self.client.get(url)

        # Assert that the user is redirected after logout
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))  # Replace 'home' with the appropriate URL name

