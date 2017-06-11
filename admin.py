from django.contrib import admin
from .models import Transport, TransportLocation, TransportUserLocation

admin.site.register(Transport)
admin.site.register(TransportLocation)
admin.site.register(TransportUserLocation)
