from django.db.models import *
from ..guest.models import Guest
from ..room.models import Room

class Booking(Model):
    room = ForeignKey(
        Room,
        verbose_name='Room',
        on_delete=CASCADE
    )

    guest = ForeignKey(
        Guest,
        verbose_name = 'Guest',
        on_delete=CASCADE
    )

    check_in_date = DateField(
        'Check in date',
        auto_now_add=True
    )

    check_out_date = DateField(
        'Check out date'
    )

    is_paid = BooleanField(
        'Is paid'
    )

    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'