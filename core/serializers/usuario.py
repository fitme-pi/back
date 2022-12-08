from djoser.serializers import UserCreateSerializer, UserSerializer
from django.contrib.auth.models import Group
from rest_framework import serializers


class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "password",
        )

    def perform_create(self, validated_data):
        user = super().perform_create(validated_data)
        user.groups.add(Group.objects.get(name="usuario"))
        return user


class CustomUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = ("id", "username", "email", "first_name", "last_name", "is_staff")
