from django.db import models

from ...account.user.user_model import Account


class Answer(models.Model):
    answer_time = models.DateTimeField()
    answer_message_text = models.CharField(
        max_length=255
    )
    answered_by = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name='answers',
        related_query_name='answer'
    )
