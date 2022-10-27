
from core.models import Usuario
from rest_framework import  serializers
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password

# Register serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id','username','password','first_name', 'last_name', 'email')
        extra_kwargs = {
            'password':{'write_only': True},
        }

    def create(self, validated_data):
        user = Usuario.objects.create_user(validated_data['username'],     password = validated_data['password']  ,first_name=validated_data['first_name'],  last_name=validated_data['last_name'])
        return user

# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
    