from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from . import models


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = models.User
        fields = ('name', 'email', 'password', 'school', 'program', 'portfolio_url', 'location', 'my_story', 'username')
