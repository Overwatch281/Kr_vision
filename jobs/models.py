from django.db import models
from accounts.models import CustomUser

class JobOffer(models.Model):
    class ContractType(models.TextChoices):
        CDI       = 'CDI',       'CDI'
        CDD       = 'CDD',       'CDD'
        STAGE     = 'stage',     'Stage'
        FREELANCE = 'freelance', 'Freelance'

    title         = models.CharField(max_length=200)
    description   = models.TextField()
    location      = models.CharField(max_length=100)
    contract_type = models.CharField(max_length=20, choices=ContractType.choices)
    is_active     = models.BooleanField(default=True)
    created_at    = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.contract_type})"


class Application(models.Model):
    class Status(models.TextChoices):
        PENDING  = 'pending',  'En attente'
        REVIEWED = 'reviewed', 'Examinée'
        ACCEPTED = 'accepted', 'Acceptée'
        REJECTED = 'rejected', 'Refusée'

    offer      = models.ForeignKey(JobOffer, on_delete=models.CASCADE, related_name='applications')
    applicant  = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='applications')
    cover_letter = models.TextField(blank=True)
    cv         = models.FileField(upload_to='cvs/')
    status     = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.applicant.username} → {self.offer.title}"