from djoser.serializers import UserCreateSerializer
from rest_framework import serializers

from core.models import Usuario


class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
        )
