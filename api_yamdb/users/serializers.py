from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import User


class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'username']
        validators = [UniqueTogetherValidator(queryset=User.objects.all(),
                                              fields=['username', 'email'])]

    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError(
                'Имя пользователя "me" не разрешено.'
            )
        return value


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

    def validate_role(self, value):
        if value not in ['user', 'moderator', 'admin']:
            raise serializers.ValidationError(
                'Роль должна быть user, moderator или admin'
            )
        return value


class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username',
                  'email',
                  'first_name',
                  'last_name',
                  'bio',
                  'role']
