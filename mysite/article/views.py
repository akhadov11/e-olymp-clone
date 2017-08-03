from django.shortcuts import render
from rest_framework import viewsets

from .models import Item
from .serializers import ItemSerializer


class ItemViewSet(viewsets.ModelViewSet, ItemSerializer):
    permission_classes = []
    serializer_class = ItemSerializer
    queryset = Item.objects.order_by(-'post_time')
