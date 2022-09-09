from rest_framework import serializers

from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')

class UserSignupSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'username')
        
class ConfirmationCodeSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=254)
    confirmation_code = serializers.CharField(max_length=254)