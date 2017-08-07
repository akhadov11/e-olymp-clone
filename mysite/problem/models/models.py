from django.db import models
from django.utils.translation import ugettext_lazy as _
# from .problem_essences import Problem


class Classification(models.Model):
    name = models.CharField(
        max_length=255
    )
    code = models.CharField(
        max_length=255
    )
    description = models.CharField(
        max_length=255
    )

    class Meta:
        verbose_name = _('Classification')
        verbose_name_plural = _('Classifications')


class Complexity(models.Model):
    name = models.CharField(
        max_length=255
    )
    code = models.CharField(
        max_length=255
    )
    description = models.CharField(
        max_length=255
    )

    class Meta:
        verbose_name = _('Complexity')
        verbose_name_plural = _('Complexities')


class Status(models.Model):
    name = models.CharField(
        max_length=255
    )
    code = models.CharField(
        max_length=255
    )
    description = models.CharField(
        max_length=255
    )

    class Meta:
        verbose_name = _('Status')
        verbose_name_plural = _('Statuses')


class Bookmark(models.Model):
    name = models.CharField(
        max_length=255
    )
    code = models.CharField(
        max_length=255
    )
    description = models.CharField(
        max_length=255
    )

    class Meta:
        verbose_name = _('Bookmark')
        verbose_name_plural = _('Bookmarks')


class Try(models.Model):
    source = models.CharField(
        max_length=255
    )
    problem = models.ForeignKey(
        'Problem'
    )

    class Meta:
        verbose_name = _('Try')
        verbose_name_plural = _('Tries')


class Test(models.Model):
    """
    input data for each test of the problem
    """
    input_data = models.CharField(
        max_length=255
    )
    problem = models.ForeignKey(
        'Problem'
    )

    class Meta:
        verbose_name = _('Test')
        verbose_name_plural = _('Tests')


class Compiler(models.Model):
    name = models.CharField(
        max_length=255
    )

    class Meta:
        verbose_name = _('Compiler')
        verbose_name_plural = _('Compilers')


class CompetitionStatus(models.Model):
    name = models.CharField(
        max_length=255
    )
    code = models.CharField(
        max_length=255
    )
    description = models.CharField(
        max_length=255
    )

    class Meta:
        verbose_name = _('CompetitionStatus')
        verbose_name_plural = _('CompetitionStatuses')


class CompetitionRule(models.Model):
    name = models.CharField(
        max_length=255
    )
    code = models.CharField(
        max_length=255
    )
    description = models.CharField(
        max_length=255
    )

    class Meta:
        verbose_name = _('CompetitionRule')
        verbose_name_plural = _('CompetitionRules')


class CompetitionType(models.Model):
    name = models.CharField(
        max_length=255
    )
    code = models.CharField(
        max_length=255
    )
    description = models.CharField(
        max_length=255
    )

    class Meta:
        verbose_name = _('CompetitionType')
        verbose_name_plural = _('CompetitionTypes')
