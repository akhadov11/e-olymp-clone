from django.shortcuts import render

from rest_framework import viewsets, mixins, response, views, permissions

from .serializers import (
    AccountSerializer, CountrySerializer, PasswordResetSerializer, UserInfoSerializer, PasswordResetConfSerializer
)
from .models.user_model import Account
from .models.models import Country
from .password_confirmation import PasswordResetConfirmation


class AccountViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny, ]
    serializer_class = AccountSerializer
    queryset = Account.objects.order_by('-last_activity')


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


class UserInfoViewSet(mixins.ListModelMixin, views.APIView):
    serializer_class = UserInfoSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        serializer = UserInfoSerializer(
            request.user
        )
        return response.Response(serializer.data)

    def put(self, request, *args, **kwargs):
        serializer = UserInfoSerializer(
            data=request.data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.update(request.user, serializer.validated_data)
        return response.Response(serializer.data)


# class EditUserInfoViewSet(mixins.UpdateModelMixin, viewsets.GenericViewSet):
#     serializer_class = UserInfoSerializer
#
#     def get_object(self):


class PasswordResetViewSet(mixins.CreateModelMixin,
                           viewsets.GenericViewSet):
    """Viewset for password reset
    """
    permission_classes = [permissions.AllowAny, ]
    serializer_class = PasswordResetConfSerializer

    def create(self, request, *args, **kwargs):
        """After checking serializer validity returns data for viewset generating.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        confirmation = serializer.save()
        response_data = serializer.data
        response_data['email'] = confirmation.user.email
        headers = self.get_success_headers(serializer.data)
        return response.Response(response_data, status=200, headers=headers)
