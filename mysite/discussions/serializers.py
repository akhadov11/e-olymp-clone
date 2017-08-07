from rest_framework import serializers

from .models.models import Deliberation
from .models.discuss_models import Answer


class DeliberationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Deliberation
        fields = ('name', 'description', 'answer', 'account')


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ('answer_message_text', 'answered_by')
