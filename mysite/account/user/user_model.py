from django.db import models
from django.contrib.auth import get_user_model

from ..models import Country
User = get_user_model()


class Account(models.Model):
    user = models.OneToOneField(
        User,
    )
    institution = models.CharField(
        max_length=255
    )
    city = models.CharField(
        null=True,
        blank=True
    )
    country = models.ForeignKey(
        Country,
        related_name='accounts',
        related_query_name='account'
    )

