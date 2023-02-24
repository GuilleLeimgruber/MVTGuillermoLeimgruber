from django.contrib import admin

# Register your models here.
from providers.models import Providers



@admin.register(Providers)
class ProviderAdmin(admin.ModelAdmin):
    list_display =('name', 'address', 'phone')
