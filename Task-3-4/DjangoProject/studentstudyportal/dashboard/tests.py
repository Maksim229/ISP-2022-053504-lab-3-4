from django.test import TestCase
from .models import User

# Create your tests here.

class TestUser(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user('test_user', email=None, password='testpass')

    def test_get_user(self):
        user = User.objects.get(username='test_user')
        self.assertTrue(user.check_password('testpass'))

    def test_main_view(self):
        response = self.client.get(f'')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/home.html')

    def test_login(self):
        login = self.client.login(username='test_user', password='testpass')
        self.client.logout()

    def test_notes(self):
        response = self.client.get(f'/notes')
        self.assertEqual(response.status_code, 302)

    def test_homework(self):
        response = self.client.get(f'/homework')
        self.assertEqual(response.status_code, 302)

    def test_todo(self):
        response = self.client.get(f'/todo')
        self.assertEqual(response.status_code, 302)

    def test_dictionary(self):
        response = self.client.get(f'/dictionary')
        self.assertEqual(response.status_code, 200)

    def test_youtube(self):
        response = self.client.get(f'/youtube')
        self.assertEqual(response.status_code, 200)

    def test_wiki(self):
        response = self.client.get(f'/wiki')
        self.assertEqual(response.status_code, 200)
