from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

from .models import Country

User = get_user_model()


class Account(models.Model):
    user = models.OneToOneField(
        User,
        related_name='account'
    )
    institution = models.CharField(
        max_length=255
    )
    last_activity = models.DateTimeField()
    city = models.CharField(
        null=True,
        blank=True,
        max_length=50
    )
    country = models.ForeignKey(
        Country,
        related_name='accounts',
        related_query_name='account',
        verbose_name=_('account')
    )

    class Meta:
        verbose_name = _('account')
        verbose_name_plural = _('accounts')
