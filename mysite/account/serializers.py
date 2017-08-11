from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers, exceptions

from .models.user_model import Account
from .models.models import Country
from .password_confirmation import PasswordResetConfirmation
from .validators import ExistingTokenValidator

User = get_user_model()


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ('institution', 'last_activity', 'city', 'country_id')
        extra_kwargs = {
            'last_activity': {'read_only': True}
        }


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

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            # TODO: add relation fields or user update from super class
            if attr == 'account':
                serializer = AccountSerializer(data=value)
                serializer.is_valid(raise_exception=True)
                serializer.update(instance.account, value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance

"""
{
    "first_name": "Test",
    "last_name": "Test",
    "email": "test@example.com",
    "last_login": "2017-08-08T14:14:26.811655Z",
    "date_joined": "2017-08-03T09:26:13.381838Z",
    "account": {
        "institution": "gfg",
        "last_activity": "2017-08-08T11:27:13.198572Z",
        "city": "kiev",
        "country": 1
    }
}
"""


class PasswordResetConfSerializer(serializers.Serializer):
    """Serializer for Password Reset.

        Attributes:
            token (str): Confirmation token (64 characters).
            new_password (str): New password.
        """
    token = serializers.CharField(
        validators=[ExistingTokenValidator(), ],
        write_only=True
    )
    new_password = serializers.CharField(
        validators=[validate_password, ],
        write_only=True
    )

    def create(self, validated_data):
        """Check validity of new password and set it.
        """
        password_reset_confirmation = PasswordResetConfirmation.objects.get(token=validated_data['token'])
        password_reset_confirmation.set_new_password(validated_data['new_password'])
        return password_reset_confirmation

    def validate_new_password(self, new_password):
        """Check whether the user really sets new password or repeats the old one.

        Returns:
            str: Password set by user
        """
        token = self.context.get('request').data.get('token')
        query = PasswordResetConfirmation.objects.filter(token=token)
        if query.exists():
            user = query.first().user
            if user.check_password(new_password):
                raise serializers.ValidationError(
                    _('This is the old password. Enter a new one.')
                )
        return new_password
