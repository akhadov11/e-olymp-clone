from rest_framework import serializers

from .models import Problem, Competition, ProblemTest


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