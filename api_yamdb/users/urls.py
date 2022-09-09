from django.urls import include, path
from rest_framework.routers import DefaultRouter

from users.views import signup_view, confirmation_view, UserViewSet

app_name = 'users'

router_v1 = DefaultRouter()
router_v1.register('users', UserViewSet)

urlpatterns = [
    path('auth/signup/', signup_view),
    path('auth/token/', confirmation_view),
    path('', include(router_v1.urls)),
]
