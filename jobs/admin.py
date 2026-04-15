from django.contrib import admin
from .models import JobOffer, Application

@admin.register(JobOffer)
class JobOfferAdmin(admin.ModelAdmin):
    list_display  = ('title', 'contract_type', 'location', 'is_active', 'created_at')
    list_filter   = ('contract_type', 'is_active')
    search_fields = ('title', 'location')

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display  = ('applicant', 'offer', 'status', 'applied_at')
    list_filter   = ('status',)
    search_fields = ('applicant__username', 'offer__title')