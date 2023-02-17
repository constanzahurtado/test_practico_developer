from django.contrib import admin
from .models import Network, Station, TableSEA

class StationInline(admin.StackedInline):
    model = Station
    extra = 0

class NetworkAdmin(admin.ModelAdmin):
    inlines = [StationInline]

admin.site.register(Network, NetworkAdmin)
admin.site.register(TableSEA)



