from rest_framework.viewsets import ModelViewSet

from .models import Guest
from .serializers import GuestSerielizer

class GuestViewSet(ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerielizer