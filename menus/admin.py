from django.contrib import admin

# Register your models here.

from menus.models import Menus, Categories



#admin.site.register(Menus)


admin.site.register(Categories)

@admin.register(Menus)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')

    list_filter = ('stock', 'price')
    search_fields = ('name',)



