from django.contrib import admin

# Register your models here.

from deliveries.models import Deliveries


#admin.site.register(Deliveries)




@admin.register(Deliveries)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('client', 'menu', 'create_time', 'payment_method')

    list_filter = ('payment_method', 'menu')

    search_fields = ('client',)
