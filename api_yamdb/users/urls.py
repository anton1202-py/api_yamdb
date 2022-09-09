from django.urls import include, path
from rest_framework.routers import DefaultRouter
from django.views.generic import TemplateView

from users.views import RegistrationAPIView, signup_view, confirmation_view

app_name = 'users'

router_v1 = DefaultRouter()
router_v1.register('users', RegistrationAPIView, basename='signup')

urlpatterns = [
    path('v1/auth/signup/', signup_view),
    path('v1/auth/token/', confirmation_view),
    path('v1/', include(router_v1.urls)),
#     path(
#         'redoc/',
#         TemplateView.as_view(template_name='redoc.html'),
#         name='redoc'
#     ),
]
