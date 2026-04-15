from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import CustomUser
from .models import Service

class HomePageTest(TestCase):
    def test_home_page_status(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_uses_correct_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

class ServiceTest(TestCase):
    def setUp(self):
        Service.objects.create(
            title='Service Test',
            description='Description test',
            is_active=True
        )

    def test_service_list_page(self):
        response = self.client.get('/services/')
        self.assertEqual(response.status_code, 200)

    def test_search_page(self):
        response = self.client.get('/search/?q=test')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Service Test')