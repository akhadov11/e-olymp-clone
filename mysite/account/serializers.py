from rest_framework import serializers

from .models.user_model import Account
from .models.models import Country


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ('institution', 'last_entrance' 'city', 'country')
        # 'models'?


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ('name',)


