from django.db import models
from django.utils.translation import ugettext_lazy as _

from .discuss_models import Answer
from mysite.account.models.user_model import Account


class Deliberation(models.Model):
    name = models.CharField(
        max_length=255
    )
    description = models.CharField(
        max_length=255
    )
    post_time = models.DateTimeField(
        auto_now_add=True
    )
    answer = models.ForeignKey(
        Answer,
        on_delete=models.CASCADE,
        related_name='deliberations',
        related_query_name='deliberation'
    )
    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name='deliberations',
        related_query_name='deliberation'
    )

    class Meta:
        verbose_name = _('deliberation')
        verbose_name_plural = _('deliberations')
