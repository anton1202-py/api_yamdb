from asyncio import run_coroutine_threadsafe
from lib2to3.pgen2 import token
from smtplib import SMTPResponseException
from urllib import response

from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, render
from rest_framework import response, status, viewsets
from rest_framework.decorators import api_view
# from rest_framework_simplejwt import RefreshToken

from users.models import User
from users.serializers import ConfirmationCodeSerializer, UserSignupSerializer, UserSerializer

# # Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



@api_view(['POST'])
def signup_view(request):
    serializer = UserSignupSerializer(data=request.data)
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
    serializer = ConfirmationCodeSerializer(data=request.data)
    serializer.is_valid()
    code = serializer.validated_data.get('confirmation_code')
    username = serializer.validated_data.get('username')
    user = get_object_or_404(User, username=username)
    if not default_token_generator.check_token(user, code):
        resp = response.Response(
            data = {'error':'некорректный токен'},
            status=status.HTTP_400_BAD_REQUEST
        )
#     token = RefreshToken.for_user(user)
    token = 123
    resp = response.Response(
            data = {'access':str(token)},
            status=status.HTTP_200_OK
        )
    return resp