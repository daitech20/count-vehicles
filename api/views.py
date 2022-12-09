from django.shortcuts import render
from .serializer import CountVehiclesSerializer
from rest_framework import viewsets
from .models import CountVehicles
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response

# Create your views here.


class FileInputViewSet(generics.CreateAPIView):
    queryset = CountVehicles.objects.all()
    serializer_class = CountVehiclesSerializer