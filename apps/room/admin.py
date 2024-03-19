from django.contrib.admin import *

from .models import Room

@register(Room)

class RoomAdmin(ModelAdmin):
    list_display = ('id', 'number', 'capacity')
    list_display_links = ('id', 'number', 'capacity')
    ordering = ('number', 'capacity')