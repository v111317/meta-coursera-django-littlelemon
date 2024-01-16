from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from .serializers import MenuItemSerializer, BookingSerializer
from .models import Booking, Menu

def say_hello(request):
    return HttpResponse("hello world")

def index(request):
    return render(request, "index.html", {})

class MenuItemsView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer
    

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Menu.objects.all()
    #lookup_url_kwarg = 'pk'
    serializer_class = MenuItemSerializer    
    
class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer