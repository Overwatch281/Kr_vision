from django.test import TestCase
from django.urls import reverse
from accounts.models import CustomUser
from .models import JobOffer, Application

class JobTest(TestCase):
    def setUp(self):
        self.job = JobOffer.objects.create(
            title='Développeur Django',
            description='Poste de dev',
            location='Paris',
            contract_type='CDI',
            is_active=True
        )
        self.user = CustomUser.objects.create_user(
            username='testuser',
            password='testpass123'
        )

    def test_job_list_page(self):
        response = self.client.get('/jobs/')
        self.assertEqual(response.status_code, 200)

    def test_job_detail_page(self):
        response = self.client.get(f'/jobs/{self.job.pk}/')
        self.assertEqual(response.status_code, 200)

    def test_apply_requires_login(self):
        response = self.client.get(f'/jobs/{self.job.pk}/apply/')
        self.assertEqual(response.status_code, 302)

    def test_apply_logged_in(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(f'/jobs/{self.job.pk}/apply/')
        self.assertEqual(response.status_code, 200)