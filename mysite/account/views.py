from django.shortcuts import render

from rest_framework import viewsets, mixins, response

from .serializers import (
    AccountSerializer, CountrySerializer, PasswordResetSerializer, UserInfoSerializer
)
from .models.user_model import Account
from .models.models import Country
from .password_confirmation import PasswordResetConfirmation


class AccountViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = AccountSerializer
    queryset = Account.objects.order_by('-last_entrance')


class CountryViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = CountrySerializer
    queryset = Country.objects.order_by('-name')


class PasswordResetConfirmationViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = PasswordResetSerializer

    def create(self, request, *args, **kwargs):
        serializer = PasswordResetSerializer(
            data=request.data,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(status=201)


class UserInfoViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = UserInfoSerializer

    def list(self, request, *args, **kwargs):
        serializer = UserInfoSerializer(
            request.user,
        )
        return response.Response(serializer.data)