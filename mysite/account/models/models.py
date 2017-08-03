from django.utils.translation import ugettext_lazy as _

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Country(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True
    )

    class Meta:
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')






