from django.shortcuts import render
from properties.models import Property
from properties.models import Room
from properties.models import RoomsType
from properties.models import Address
from properties.models import Reviews
from properties.models import Booking
# Create your views here.


def property_view(request):
    property_list = Property.objects.all()

    context = {'property_list_view': property_list}
    return render(request, 'properties/property.html', context)


def room_view(request):
    room_list = Room.objects.all()

    context = {'room_list_view': room_list}
    return render(request, 'properties/room.html', context)


def rooms_type_view(request):
    rooms_type_list = RoomsType.objects.all()

    context = {'rooms_type_list_view': rooms_type_list}
    return render(request, 'properties/rooms_type.html', context)


def address_view(request):
    address_list = Address.objects.all()

    context = {'address_view': address_list}
    return render(request, 'properties/address.html', context)


def reviews_view(request):
    reviews_list = Reviews.objects.all()

    context = {'reviews_view': reviews_list}
    return render(request, 'properties/reviews.html', context)


def booking_view(request):
    booking_list = Booking.objects.all()

    context = {'booking_view': booking_list}
    return render(request, 'properties/booking.html', context)
