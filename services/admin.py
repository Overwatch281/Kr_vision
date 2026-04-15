from django.contrib import admin
from .models import Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display  = ('title', 'is_active', 'order')
    list_editable = ('is_active', 'order')
    search_fields = ('title',)

from .models import Service, Partner

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display  = ('name', 'website', 'is_active')
    list_editable = ('is_active',)