from rest_framework import serializers

from .models import User


class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'username']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class AuthentificationSerializer(serializers.ModelSerializer):
    confirmation_code = serializers.CharField(max_length=255, write_only=True)
    username = serializers.CharField(max_length=255)

    class Meta:
        model = User
        fields = ['username', 'confirmation_code']


class UserSerializer(serializers.ModelSerializer):
    role = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ['username',
                  'email',
                  'first_name',
                  'last_name',
                  'bio',
                  'role']


class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username',
                  'email',
                  'first_name',
                  'last_name',
                  'bio',
                  'role']
