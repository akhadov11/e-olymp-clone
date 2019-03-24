from django.db import models
from django.utils.translation import ugettext_lazy as _

from ...account.models.user_model import Account


class Answer(models.Model):
    answer_time = models.DateTimeField(
        auto_now_add=True
    )
    answer_message_text = models.CharField(
        max_length=255
    )
    answered_by = models.OneToOneField(
        Account,
        on_delete=models.CASCADE,
        related_name='answers',
    )

    class Meta:
        verbose_name = _('answer')
        verbose_name_plural = _('answers')
