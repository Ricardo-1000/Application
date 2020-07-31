from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.conf import settings
#from django.contrib.auth.models import User
# Create your models here.


class Address(models.Model):

    country = models.CharField(max_length=255, default='Romania')
    state = models.CharField(max_length=255, default='Dolj')
    city = models.CharField(max_length=255, default='Craiova')
    street = models.CharField(max_length=255, )
    street_no = models.DecimalField(max_digits=8, decimal_places=0)
    details = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.country


class Property(models.Model):
    STATUS = (
            ('Available', 'Available'),
            ('Unavailable', 'Unavailable'),
            )
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, default='Romania')
    image = models.ImageField(upload_to='property_picture/', blank=True, null=True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=200, null=False, choices=STATUS)
    address = models.ForeignKey(Address, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Room(models.Model):
    STATUS = (
            ('Available', 'Available'),
            ('Unavailable', 'Unavailable'),
            )
    name = models.CharField(max_length=255, default='Room')
    price = models.DecimalField(max_digits=8, decimal_places=2, default=150.99)
    status = models.CharField(max_length=200, null=False, choices=STATUS)
    property = models.ForeignKey(Property, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Reviews(models.Model):
    REVIEW = (
            ('*', '*'),
            ('**', '**'),
            ('***', '***'),
            ('****', '****'),
            ('*****', '*****'),)

    review = models.CharField(max_length=200, null=False, choices=REVIEW)
    comment = models.CharField(max_length=255)
    property = models.OneToOneField(Property, null=True, on_delete=models.CASCADE)
    user_id = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    #user_id = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.property.name


class RoomsType(models.Model):
    BED_TYPE = (
            ('Single', 'Single'),
            ('Double', 'Double'),
            ('Queen', 'Queen'),
            ('King', 'King'),
            )

    BATHROOM_TYPE = (
            ('Communal', 'Communal'),
            ('Private', 'Private'),
            )

    name = models.CharField(max_length=255, default='Room')
    bed_count = models.DecimalField(max_digits=8, decimal_places=0)
    bed_type = models.CharField(max_length=200, null=False, choices=BED_TYPE)
    bathroom_type = models.CharField(max_length=200, null=False, choices=BATHROOM_TYPE)
    room_id = models.ForeignKey(Room, null=True, on_delete=models.SET_NULL)
    icon_image = models.ImageField(upload_to='room_picture', blank=True, null=True)

    def __str__(self):
        return self.name


class Booking(models.Model):

    room_id = models.ForeignKey(Room, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    adults = models.DecimalField(max_digits=8, decimal_places=0)
    childrens = models.DecimalField(max_digits=8, decimal_places=0)
    check_in_date = models.DateTimeField(default=timezone.now)
    check_out_date = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.DecimalField(max_digits=15, decimal_places=0)

    def __str__(self):
        return self.name
