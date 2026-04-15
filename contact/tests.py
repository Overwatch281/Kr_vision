from django.test import TestCase
from .models import Message, Newsletter

class ContactTest(TestCase):
    def test_contact_page(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)

    def test_send_message(self):
        response = self.client.post('/contact/', {
            'name':    'Jean Dupont',
            'email':   'jean@test.com',
            'subject': 'Test',
            'body':    'Message de test',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Message.objects.count(), 1)

    def test_newsletter_subscribe(self):
        response = self.client.post('/contact/newsletter/', {
            'email': 'newsletter@test.com'
        })
        self.assertEqual(Newsletter.objects.count(), 1)