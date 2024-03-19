# from rest_framework.viewsets import ModelViewSet

from .models import Hotel
# from .serializers import HotelSerializer

from django.shortcuts import render

from django.views.generic import (
    ListView,
    DetailView
)
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
    
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# class HotelViewSet(ModelViewSet):
#     queryset = Hotel.objects.all()
#     serializer_class = HotelSerializer



class HotelList(ListView):

    model = Hotel
    template_name = 'hotel/hotels.html'
    context_object_name = 'hotels'

class HotelDetail(DetailView):

    model = Hotel
    template_name = 'hotel/hotel-detail.html'
    context_object_name = 'hotel-detail'

class HotelCreate(LoginRequiredMixin, CreateView):
    model = Hotel
    template_name = 'hotel/hotel-create.html'
    context_object_name = 'hotel-create'
    fields = '__all__'
    success_url = reverse_lazy('hotels')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class HotelUpdate(UpdateView):
    model = Hotel
    template_name = 'hotel/hotel-update.html'
    context_object_name = 'hotel-update'
    fields = '__all__'

    success_url = reverse_lazy('hotels')

class HotelDelete(DeleteView):
    model = Hotel
    template_name = 'hotel/hotel-delete.html'
    context_object_name = 'hotel-delete'
    success_url = reverse_lazy('hotels')

def my_hotels(request):
    hotels = Hotel.objects.filter(author=request.user)
    context = {
        'hotels': hotels
    }
    return render(request, 'hotel/my-hotels.html', context=context)