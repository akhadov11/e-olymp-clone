from django.db import models

from .discuss_models import Answer
from mysite.account.user.user_model import Account


class Deliberation(models.Model):
    name = models.CharField(
        max_length=255
    )
    description = models.CharField(
        max_length=255
    )
    post_time = models.CharField(
        max_length=255
    )
    answer_time = models.CharField(
        max_length=255
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
