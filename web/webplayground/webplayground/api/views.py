from django.shortcuts import render
from rest_framework import generics

from merchants.models import Merchant
from ongs.models import Ong

from .serializers import MerchantSerializer, OngSerializer

class MerchantApiView(generics.ListAPIView):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer

class OngApiView(generics.ListAPIView):
    queryset = Ong.objects.all()
    serializer_class = OngSerializer

