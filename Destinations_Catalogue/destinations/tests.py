# from django.contrib.auth import get_user_model
# from django.test import TestCase, Client
# from django.urls import reverse
#
#
#
# class DestinationCreateViewTest(TestCase):
#     def setUp(self):
#         # self.client = Client()
#         self.user = get_user_model().objects.create_user(
#             username='testuser',
#             password='testpassword'
#         )
#         # self.client.login(username='testuser', password='testpassword')
#
#     def test_something_view(self):
#         client = Client()
#         client.force_login(self.user)
#         response = client.post(reverse('home'), follow=True)
#         self.assertEqual(response.status_code, 200)