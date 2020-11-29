from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from pz_project_todo_list.todo_list.models import TodoList


class TodoListsTest(APITestCase):
    def test_create_list(self):
        title = 'Test list create'

        response = self.client.post(reverse('todo-lists-list'),
                                    {'title': title},
                                    format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(TodoList.objects.count(), 1)
        self.assertEqual(TodoList.objects.get().title, title)

    def test_update_list(self):
        todo_list = TodoList()
        todo_list.title = 'Test list update'
        todo_list.save()

        new_title = 'THIS IS NEW TITLE'

        response = self.client.put(reverse('todo-lists-detail', args=[todo_list.id]),
                                   {'title': new_title},
                                   format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(TodoList.objects.count(), 1)
        self.assertEqual(TodoList.objects.get().title, new_title)
