from django.shortcuts import render
from rest_framework import viewsets

from .models import Competition, Problem, ProblemTest
from .serializers import (
    CompetitionSerializer, ProblemSerializer, ProblemTestSerializer
)


class CompetitionViewSet(viewsets.ModelViewSwt):
    permission_classes = []
    serializer_class = CompetitionSerializer
    queryset = Competition.objects.order_by('-creation_time')


class ProblemViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = ProblemSerializer


class ProblemTestViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = ProblemTestSerializer
