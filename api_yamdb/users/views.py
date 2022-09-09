from rest_framework import response, status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404, render
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.decorators import api_view
from smtplib import SMTPResponseException
from django.contrib.auth.tokens import default_token_generator

from users.models import User
from users.serializers import RegistrationSerializer, UserSerializer, AuthentificationSerializer


class RegistrationAPIView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



@api_view(['POST'])
def signup_view(request):
    serializer = RegistrationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    username = serializer.validated_data.get('username')
    if username == 'me':
        resp = response.Response(
            data={
                'error':"Нельзя использовать me в качестве имени"
            },
            status=status.HTTP_400_BAD_REQUEST
        )
    email = serializer.validated_data.get('email')
    user, created = User.objects.get_or_create(username=username, 
                                               email=email)

    if not created:
        resp = response.Response(
            data={
                'error':"Пользователь с таким именем или эмейлом существует"
            },
            status=status.HTTP_400_BAD_REQUEST
        )
    token = default_token_generator.make_token(user)
    try:
        send_mail(
            'Token',
            f'{token}',
            f'{settings.MAILING_EMAIL}',
            [email]
        )
        resp = response.Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )
    except SMTPResponseException:
        resp = response.Response(
            data={
                'error':"Не получилось отправить эмейл"
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    return resp
        
@api_view(['POST'])
def confirmation_view(request):
    serializer = AuthentificationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    code = serializer.validated_data.get('confirmation_code')
    username = serializer.validated_data.get('username')
    print(username)
    user = get_object_or_404(User, username=username)
    print('found')
    if not default_token_generator.check_token(user, code):
        resp = response.Response(
            data = {'error':'некорректный токен'},
            status=status.HTTP_400_BAD_REQUEST
        )
    token = user.token
    resp = response.Response(
            data = {'access':str(token)},   
            status=status.HTTP_200_OK
        )
    return resp