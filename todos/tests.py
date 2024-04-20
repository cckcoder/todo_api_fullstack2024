from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from .models import Todo


class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.todo = Todo.objects.create(
            title="First todo",
            body="This is body"
        )

    def test_title_content(self):
        todo = Todo.objects.get(id=1)
        expected_title = f"{todo.title}"
        self.assertEqual(expected_title, "First todo")

    def test_body_content(self):
        todo = Todo.objects.get(id=1)
        expected_body = f"{todo.body}"
        self.assertEqual(expected_body, "This is body")

    def test_api_listview(self):
        response = self.client.get(reverse("todo_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, self.todo)

    def test_api_detailview(self):
        response = self.client.get(
            reverse("todo_detail", kwargs={"pk": self.todo.id}),
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, "First todo")