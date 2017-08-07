from django.shortcuts import render
from rest_framework import viewsets

from .models import (
    Competition, Problem, ProblemTest,
    Classification, Complexity, Status, Bookmark,
    Compiler, Try, Test,
    CompetitionStatus, CompetitionRule, CompetitionType,
)
from .serializers import (
    CompetitionSerializer, ProblemSerializer, ProblemTestSerializer,
    ClassificationSerializer, ComplexitySerializer, StatusSerializer, BookmarkSerializer,
    TrySerializer, CompilerSerializer, TestSerializer,
    CompetitionRuleSerializer, CompetitionStatusSerializer, CompetitionTypeSerializer,
)


class CompetitionViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = CompetitionSerializer
    queryset = Competition.objects.order_by('-creation_time')


class ProblemViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = ProblemSerializer
    queryset = Problem.objects.all()


class ProblemTestViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = ProblemTestSerializer
    queryset = ProblemTest.objects.all()


class ClassificationVieSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = ClassificationSerializer
    queryset = Classification.objects.all()


class ComplexityVieSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = ComplexitySerializer
    queryset = Complexity.objects.all()


class StatusViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = StatusSerializer
    queryset = Status.objects.all()


class BookmarkViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = BookmarkSerializer
    queryset = Bookmark.objects.all()


class TryViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_classes = TrySerializer
    queryset = Try.objects.all()


class TestViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = TestSerializer
    queryset = Test.objects.all()


class CompilerViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = CompilerSerializer
    queryset = Compiler.objects.all()


class CompetitionRuleViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = CompetitionRuleSerializer
    queryset = CompetitionRule.objects.all()


class CompetitionTypeViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = CompetitionTypeSerializer
    queryset = CompetitionType.objects.all()


class CompetitionStatusViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = CompetitionStatusSerializer
    queryset = CompetitionStatus.objects.all()
