from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers

from .password_confirmation import PasswordResetConfirmation


User = get_user_model()


class ExistingTokenValidator(object):
    """Validator to check if token provided for pwd reminding is valid
    """

    def __call__(self, token):
        if not PasswordResetConfirmation.is_valid(token):
            raise serializers.ValidationError(
                _('Wrong token.')
            )
