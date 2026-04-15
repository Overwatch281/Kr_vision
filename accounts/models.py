from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        VISITOR   = 'visitor',   'Visiteur'
        CLIENT    = 'client',    'Client / Candidat'
        PARTNER   = 'partner',   'Partenaire'
        ADMIN     = 'admin',     'Administrateur'

    role        = models.CharField(max_length=20, choices=Role.choices, default=Role.VISITOR)
    phone       = models.CharField(max_length=20, blank=True)
    company     = models.CharField(max_length=100, blank=True)
    avatar      = models.ImageField(upload_to='avatars/', blank=True, null=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"