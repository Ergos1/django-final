from django.urls import include, path

from .views import list_user, UserViewSet, BookViewSet, JournalViewSet
from rest_framework import routers

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

app_name = "api"
router = routers.DefaultRouter()
router.register(r'auth', UserViewSet, basename="Auth user")
router.register(r'api/books', BookViewSet, basename="Book")
router.register(r'api/journals', JournalViewSet, basename="Journal")

urlpatterns = [
    path('', include(router.urls)),
    path('api/users/', list_user, name="user_list"),
    path('auth/login/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
]