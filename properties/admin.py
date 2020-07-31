from django.contrib import admin
from properties.models import Property
from properties.models import Room
from properties.models import RoomsType
from properties.models import Address
from properties.models import Reviews
from properties.models import Booking

# Register your models here.
admin.site.register(Property)
admin.site.register(Room)
admin.site.register(RoomsType)
admin.site.register(Address)
admin.site.register(Reviews)
admin.site.register(Booking)
