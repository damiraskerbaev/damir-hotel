from django.db.models import *

from ..hotel.models import Hotel

class Room(Model):

    Hotel = ForeignKey(
        Hotel,
        verbose_name='Hotel',
        on_delete=CASCADE
    )

    number = PositiveIntegerField(
        'Number of the room'
    )

    capacity = PositiveIntegerField(
        'Capacity of the room'
    )

    price_per_night = PositiveBigIntegerField(
        'Price per night'
    )

    is_used = BooleanField(
        'Is used'
    )

    description = TextField(
        'Description of the room',
        blank=True
    )

    def __str__(self):
        return f'{self.number}'
    
    class Meta:
        verbose_name='Room'
        verbose_name_plural='Rooms'