from django.shortcuts import render
from .serializers import UserSerializer, MenuSerializer,BookingSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, AllowAny

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Menu, Booking

"""
# Create your views here.
def index(request):
    return render(request, 'index.html', {})

"""


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


"""
class UserListCreateView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class UserRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
"""

class MenuItemView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]