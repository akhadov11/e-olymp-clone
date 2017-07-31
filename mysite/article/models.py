from django.db import models

from ..account.user.user_model import Account

class item(models.Model):
    name = models.CharField(
        max_length=255
    )
    description = models.CharField(
        max_length=255
    )
    post_time = models.CharField(
        max_length=255
    )
    created_by = models.ForeignKey(
        Account,
        related_name='items',
        related_query_name='item'
    )
