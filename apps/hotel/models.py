from django.db.models import *

class Hotel(Model):

    name = CharField(
        'Hotel of the name',
        max_length=128
    )

    address = CharField(
        'Address of the hotel',
        max_length=512
    )

    city = CharField(
        'City',
        max_length=64
    )

    country = CharField(
        'Country',
        max_length=64
    )

    rating = DecimalField(
        'Rating of the hotel',
        decimal_places=1,
        max_digits=7
    )

    image = ImageField(
        'Image of the Hotel',
        upload_to='hotels/%Y/%m/%d'
    )

    description = TextField(
        'Descrtiption of the Hotel'
    )

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name='Hotel'
        verbose_name_plural='Hotels'