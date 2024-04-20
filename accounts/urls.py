
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path

from .views import UserListCreateView, UserDetailView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("<int:pk>/", UserDetailView.as_view(), name="user_detail"),
    path("", UserListCreateView.as_view(), name="user_list")
]
