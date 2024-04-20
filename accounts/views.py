from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from .serializers import UserSerializer, UserDetailSerializer
from .models import User


class UserListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer