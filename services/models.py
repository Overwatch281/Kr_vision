from django.db import models

class Service(models.Model):
    title       = models.CharField(max_length=200)
    description = models.TextField()
    icon        = models.CharField(max_length=50, blank=True)
    image       = models.ImageField(upload_to='services/', blank=True, null=True)
    is_active   = models.BooleanField(default=True)
    order       = models.PositiveIntegerField(default=0)
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title
    

class Partner(models.Model):
    name      = models.CharField(max_length=200)
    logo      = models.ImageField(upload_to='partners/', blank=True, null=True)
    website   = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name