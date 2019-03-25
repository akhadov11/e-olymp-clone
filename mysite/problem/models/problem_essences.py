from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

from .models import (
    Classification, Complexity, Status, Bookmark,
    Try, Compiler, Test,
    CompetitionStatus, CompetitionRule, CompetitionType,
)

User = get_user_model()


class Competition(models.Model):
    name = models.CharField(
        max_length=255,
    )
    description = models.CharField(
        max_length=255
    )
    status = models.ForeignKey(
        CompetitionStatus,
        on_delete=models.CASCADE,
        related_name='competitions',
        related_query_name='competition'
    )
    rule = models.ForeignKey(
        CompetitionRule,
        on_delete=models.CASCADE,
        related_name='competitions',
        related_query_name='competition'
    )
    type = models.ForeignKey(
        CompetitionType,
        on_delete=models.CASCADE,
        related_name='competitions',
        related_query_name='competition'
    )
    creation_time = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name = _('Competition')
        verbose_name_plural = _('Competitions')


class ProblemTest(models.Model):

    """
    testing of the whole problem
    """

    attempt = models.ForeignKey(
        Try,
        on_delete=models.CASCADE,
        related_name='ProblemTests',
        related_query_name='ProblemTest'
    )
    compiler = models.ForeignKey(
        Compiler,
        on_delete=models.CASCADE,
        related_name='ProblemTests',
        related_query_name='ProblemTest'
    )
    test = models.ForeignKey(
        Test,
        on_delete=models.CASCADE,
        related_name='ProblemTests',
        related_query_name='ProblemTest'
    )

    class Meta:
        verbose_name = _('ProblemTest')
        verbose_name_plural = _('ProblemTests')


class Problem(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True
    )
    point = models.IntegerField()
    competition = models.ForeignKey(
        Competition,
        on_delete=models.CASCADE,
        related_name='problems',
        related_query_name='problem'
    )
    classification = models.ForeignKey(
        Classification,
        on_delete=models.CASCADE,
        related_name='problems',
        related_query_name='problem'
    )
    complexity = models.ForeignKey(
        Complexity,
        on_delete=models.CASCADE,
        related_name='problems',
        related_query_name='problem'
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE,
        related_name='problems',
        related_query_name='problem'
    )
    bookmark = models.ForeignKey(
        Bookmark,
        on_delete=models.CASCADE,
        related_name='problems',
        related_query_name='problem'
    )

    class Meta:
        verbose_name = _('Problem')
        verbose_name_plural = _('Problems')
