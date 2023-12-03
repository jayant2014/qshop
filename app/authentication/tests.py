# authentication/tests.py
from django.test import TestCase
from django.contrib.auth.models import User

class AuthenticationTests(TestCase):
    def test_profile_view(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/profile.html')
