from django.contrib.auth import get_user_model

from rest_framework import serializers, exceptions

from .models.user_model import Account
from .models.models import Country
from .password_confirmation import PasswordResetConfirmation


User = get_user_model()


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ('institution', 'last_activity', 'city', 'country')


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ('name',)


def validate_email_existance(value):
    if not User.objects.filter(email=value).exists():
        raise exceptions.ValidationError('Email {0} does not exist'.format(value))


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField(validators=[validate_email_existance])

    def create(self, validated_data):
        user = User.objects.get(
            email=validated_data['email'],
        )
        confirmation = PasswordResetConfirmation.create(user)
        confirmation.send_reset_link()
        return confirmation


class UserInfoSerializer(serializers.ModelSerializer):
    account = AccountSerializer()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'last_login', 'date_joined', 'account')
