from django.contrib import admin

# Register your models here.

from reservations.models import Reservations


#admin.site.register(Reservations)



@admin.register(Reservations)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'dinner', 'reservation_date')

    list_filter = ('reservation_date',)

    search_fields = ('name',)


