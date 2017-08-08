from django.shortcuts import render
from rest_framework import viewsets

from .models.models import Deliberation
from .models.discuss_models import Answer
from .serializers import DeliberationSerializer, AnswerSerializer


class DeliberationViewSet(viewsets.ModelViewSet, DeliberationSerializer):
    permission_classes = []
    serializer_class = DeliberationSerializer
    queryset = Deliberation.objects.order_by('-post_time')


class AnswerViewSet(viewsets.ModelViewSet, AnswerSerializer):
    permission_classes = []
    serializer_class = AnswerSerializer
    queryset = Answer.objects.order_by('-answer_time')
