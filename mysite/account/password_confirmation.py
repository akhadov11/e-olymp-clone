import datetime
import logging

from django.db import models, transaction
from django.utils import timezone
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _

from .hooks import (
    send_password_reset_email, send_password_change_email, generate_email_confirmation_token
)
from .utils import get_service_host
User = get_user_model()

logger = logging.getLogger(__name__)


class Error(Exception):
    """Base error for this module."""


class ConfirmationBase(models.Model):
    """Base class for confirmation models.

    Attributes:
        token (str): Confirmation token (64 characters).
        user (:class:`~.User`): User.
        confirmed_on (datetime.datetime or None): Confirmation time.
        created_on (datetime.datetime): Entry creation time.
        last_modified_on (datetime.datetime): Entry last update time.

    """

    class AlreadyConfirmed(Error):
        pass

    token = models.CharField(
        max_length=64,
        unique=True
    )
    user = models.ForeignKey(
        User
    )
    confirmed_on = models.DateTimeField(
        null=True
    )
    created_on = models.DateTimeField(
        auto_now_add=True
    )
    last_modified_on = models.DateTimeField(
        auto_now=True
    )

    @property
    def expiration(self):
        """datetime.datetime: Expiration time."""
        return self.created_on + datetime.timedelta(
            days=settings.ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS
        )

    @property
    def expired(self):
        """bool: Whether expiration time passed."""
        return self.expiration <= timezone.now()

    @property
    def confirmed(self):
        """bool: Whether confirmation used."""
        return self.confirmed_on is not None

    @property
    def current_site(self):
        """contrib.sites.models.Site: Current site, passed to email templates context."""
        return Site.objects.get_current()

    @classmethod
    def create(cls, user, **kwargs):
        """Create confirmation for email.

        Returns:
            :class:`~.ConfirmationBase`: Confirmation for an email.
        """
        token = generate_email_confirmation_token(user.email)
        return cls.objects.create(user=user, token=token, **kwargs)

    @classmethod
    def is_valid(cls, token):
        """Check whether a token is valid.

        Returns:
            bool: Token validity.
        """
        query = cls.objects.filter(token=token)
        if query.exists():
            confirmation = query.first()
            if not confirmation.expired and not confirmation.confirmed:
                return True
        return False

    def confirm(self):
        """Confirm."""
        if self.confirmed_on is None:
            self.confirmed_on = timezone.now()
            self.save()
        else:
            raise self.AlreadyConfirmed()

    class Meta:
        abstract = True


class PasswordResetConfirmation(ConfirmationBase):
    """Confirmation of password resetting."""

    registration = models.BooleanField(default=False)

    def send_reset_link(self, **kwargs):
        """Send an email with a link for password resetting.

        Keyword Args:
            site (str): 'site' can be included, by default domain will ba a current_site from site app.
        """
        if self.is_valid(self.token):
            current_site = kwargs["site"] if "site" in kwargs else self.current_site
            service_url = get_service_host()
            activate_url = "{0}{1}".format(
                service_url,
                # TODO: use reverse here
                # reverse(settings.ACCOUNT_EMAIL_CONFIRMATION_URL, args=[self.key])
                '/reset-password/{token}/'.format(token=self.token)
            )
            ctx = {
                "email_address": self.user.email,
                "user": self.user,
                "password_reset_url": activate_url,
                "current_site": current_site,
                "key": self.token,
                "service_url": service_url,
            }
            send_password_reset_email([self.user.email], ctx)
            # TODO: add signal
        else:
            raise Exception('Invalid token.')

    def after_password_changed(self, **kwargs):
        """Send an email that notifies about password change.

        Keyword Args:
            site (str): 'site' can be included, by default domain will ba a current_site from site app.
        """
        current_site = kwargs["site"] if "site" in kwargs else self.current_site
        # TODO: add now() method to User model
        # current_time = self.user.now()
        service_url = get_service_host()
        current_time = timezone.now()
        ctx = {
            "email_address": self.user.email,
            "user": self.user,
            "current_site": current_site,
            "now": current_time,
            "service_url": service_url,
        }
        send_password_change_email([self.user.email], ctx)

    def set_new_password(self, new_password):
        self.user.set_password(new_password)
        self.user.save()
        self.confirm()

    @transaction.atomic()
    def confirm(self):
        """Called after setting a new password. Sets confirmation time and fires event about password resetting."""
        if self.is_valid(self.token):
            # TODO: some actions before sending email about password resetting
            super(PasswordResetConfirmation, self).confirm()
            # TODO: add signal
            return True
        else:
            return False

    def __str__(self):
        return 'Password reset confirmation for %s' % self.user

    class Meta:
        verbose_name = _("Password reset confirmation")
        verbose_name_plural = _("Password reset confirmations")
