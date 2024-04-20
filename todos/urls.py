from django.urls import path

from .views import ListTodo, DetailTodo

urlpatterns = [
    path("<int:pk>/", DetailTodo.as_view(), name="todo_detail"), # api/todos/<id>/
    path("", ListTodo.as_view(), name="todo_list")
]
