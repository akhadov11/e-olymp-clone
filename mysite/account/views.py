from django.shortcuts import render
from rest_framework import viewsets

from .serializers import AccountSerializer, CountrySerializer
from .models.user_model import Account


class AccountViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = AccountSerializer
    Account.objects.order_by(-'last_entrance')


class CountryViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = CountrySerializer
    Country.objects.order_by('name')