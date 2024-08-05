from django.contrib import admin
from .models import Location, Provider, Service
# Register your models here.


admin.site.register(Location)
admin.site.register(Provider)
admin.site.register(Service)
