from django.contrib.auth.models import User
from django.core.serializers import serialize
from django.db.models.query_utils import select_related_descend
from rest_framework import serializers

from main.models import Hall, Client


class HallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hall
        fields = ['id', 'name', 'city', 'address', 'price']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 'username', 'email']


class ClientSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Client
        fields = ['id', 'user', 'address']
