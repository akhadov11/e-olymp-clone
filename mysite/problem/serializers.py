from rest_framework import serializers

from .models import (
    Problem, Competition, ProblemTest,
    Complexity, Classification, Status, Bookmark,
    Try, Compiler, Test,
    CompetitionRule, CompetitionType, CompetitionStatus,
)


class ProblemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Problem
        fields = ('name', 'description', 'classification', 'complexity', 'status', 'bookmark')


class CompetitionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Competition
        fields = ('name', 'description', 'status', 'rule', 'type')


class ProblemTestSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProblemTest
        fields = ('try-id', 'compiler', 'test')


class ComplexitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Complexity
        fields = ('name', 'description')


class ClassificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Classification
        fields = ('name', 'description')


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ('name', 'description')


class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ('name', 'description')


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ('name',)


class TrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Try
        fields = ('name',)


class CompilerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compiler
        fields = ('name',)


class CompetitionRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompetitionRule
        fields = ('name', 'description')


class CompetitionStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompetitionStatus
        fields = ('name', 'description')


class CompetitionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompetitionType
        fields = ('name', 'description')
