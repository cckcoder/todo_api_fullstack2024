from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Todo
from .serializers import TodoSerializer


"""
CRUD Operation
C = Create
R = Read
U = Update
D = Delete
"""
class ListTodo(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Todo.objects.all().order_by('-id')
    serializer_class = TodoSerializer


class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all().order_by('-id')
    serializer_class = TodoSerializer
