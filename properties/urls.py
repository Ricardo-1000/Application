from django.urls import path
from properties.views import property_view
from properties.views import room_view
from properties.views import rooms_type_view
from properties.views import address_view
from properties.views import booking_view
from properties.views import reviews_view


app_name = 'properties'

urlpatterns = [path('', view=property_view, name='properties'),
               path('rooms/', view=room_view, name='rooms'),
               path('rooms/rooms_type/', view=rooms_type_view, name='rooms_type'),
               path('address/', view=address_view, name='address'),
               path('booking/', view=booking_view, name='booking'),
               path('reviews/', view=reviews_view, name='reviews'),
               ]

