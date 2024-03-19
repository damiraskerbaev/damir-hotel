from rest_framework.serializers import *

from .models import Booking

class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'