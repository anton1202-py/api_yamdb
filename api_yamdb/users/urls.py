from django.urls import include, path
from rest_framework.routers import DefaultRouter

from users.views import signup_view, confirmation_view, UserViewSet

app_name = 'users'

router_v1 = DefaultRouter()
router_v1.register('users', UserViewSet)

urlpatterns = [
    path('signup/', signup_view),
    path('token/', confirmation_view),
    path('me/', confirmation_view),
    path('v1/', include(router_v1.urls)),
]
