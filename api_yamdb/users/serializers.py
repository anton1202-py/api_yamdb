from rest_framework import serializers

from users.models import User


class UserSignupSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'username')
        
    