from django.db import models
from django.utils.translation import ugettext_lazy as _

from account.models.user_model import Account


class Item(models.Model):
    name = models.CharField(
        max_length=255
    )
    description = models.CharField(
        max_length=255
    )
    post_time = models.DateTimeField(
        auto_now_add=True
    )
    created_by = models.OneToOneField(
        Account,
        related_name='items',
        related_query_name='item',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = _('item')
        verbose_name_plural = _('items')

