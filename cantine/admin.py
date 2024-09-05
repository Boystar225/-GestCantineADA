from django.contrib import admin
from .models.menu_model import Menu
from .models.plat_model import Plat

class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'creation_date')
    search_fields = ('id',)

class PlatAdmin(admin.ModelAdmin):
    list_display = ('name', 'summary', 'id')
    search_fields = ('name', 'summary')
    list_filter = ('id',)

admin.site.register(Menu, MenuAdmin)
admin.site.register(Plat, PlatAdmin)
