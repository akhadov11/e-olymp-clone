from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

User = get_user_model()


class Country(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')
