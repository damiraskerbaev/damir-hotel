from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import HotelList, HotelDetail, HotelCreate, HotelUpdate, HotelDelete, my_hotels

# router = DefaultRouter()
# router.register('hotel', HotelViewSet, basename='hotel')

urlpatterns = [
    path('hotel/', HotelList.as_view(), name='hotel_list'),
    path('hotel/<int:pk>/', HotelDetail.as_view(), name='hotel_detail'),
    path('hotel/create/', HotelCreate.as_view(), name='hotel_create'),
    path('hotel/update/<int:pk>/', HotelUpdate.as_view(), name='hotel_update'),
    path('hotel/delete/<int:pk>/', HotelDelete.as_view(), name='hotel_delete')
]